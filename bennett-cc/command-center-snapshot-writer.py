#!/usr/bin/env python3
"""Fail-closed Function Command Center snapshot writer.

Tries QB / Meta / GHL. If auth fails, emit BLOCKED + SAMPLE_FIXTURE_NOT_REAL.
Never invent live dollars. Never treat personal QB as FKI.
Missing speed-to-lead log → RED, never 4.0 / 8.1.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
DEFAULT_OUT = OUT_DIR / "command-center-snapshot-latest.json"
SPEED_LOG = Path(os.environ.get("CC_SPEED_TO_LEAD_LOG", str(OUT_DIR / "speed-to-lead.log")))
FKI_QB_REALM_ALLOW = {"fki", "franchise-ki", "franchise ki", "fki llc"}
CANARY_RECEIPT = OUT_DIR / "false-green-canary-latest.json"


def resolve_out(argv=None):
    """Canary/tests must not mutate production. Prefer --out, then CC_SNAPSHOT_OUT."""
    args = list(sys.argv[1:] if argv is None else argv)
    for i, a in enumerate(args):
        if a == "--out" and i + 1 < len(args):
            return Path(args[i + 1])
        if a.startswith("--out="):
            return Path(a.split("=", 1)[1])
    env = os.environ.get("CC_SNAPSHOT_OUT", "").strip()
    if env:
        return Path(env)
    return DEFAULT_OUT


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def try_cmd(argv, timeout=20):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout or "").strip(), (r.stderr or "").strip()
    except Exception as e:
        return 2, "", str(e)


def probe_qb():
    """Return (ok, realm_id, cash, blocker). Never use personal realm as FKI."""
    realm = os.environ.get("FKI_QB_REALM_ID") or os.environ.get("QB_REALM_ID") or ""
    realm_label = os.environ.get("FKI_QB_REALM_LABEL", "").strip().lower()
    if not realm:
        # Probe common local helpers; absence is BLOCKED, not $0.
        for probe in (
            ["python3", os.path.expanduser("~/.openclaw/scripts/qb-cash-pull.py")],
            ["gog", "quickbooks", "companyinfo"],
        ):
            if Path(probe[1]).exists() if probe[0] == "python3" else True:
                rc, out, err = try_cmd(probe[:2] if probe[0] != "python3" else probe)
                if rc == 0 and out:
                    try:
                        data = json.loads(out)
                        realm = str(data.get("qb_realm_id") or data.get("realmId") or "")
                        label = str(data.get("realm_label") or data.get("CompanyName") or "").lower()
                        if label and not any(x in label for x in FKI_QB_REALM_ALLOW):
                            return False, realm, None, f"QB realm looks personal/non-FKI: {label[:80]}"
                        cash = data.get("cash")
                        return True, realm, cash, ""
                    except Exception:
                        pass
        return False, "", None, "QB auth missing — live FKI realm not re-pulled"
    if realm_label and not any(x in realm_label for x in FKI_QB_REALM_ALLOW):
        return False, realm, None, f"QB realm labeled personal/non-FKI: {realm_label}"
    return False, realm, None, "QB realm id present in env but live pull helper not authenticated"


def probe_meta():
    rc, out, err = try_cmd(["python3", "-c", "import os; print(os.environ.get('META_ACCESS_TOKEN',''))"])
    token = os.environ.get("META_ACCESS_TOKEN") or os.environ.get("FB_ACCESS_TOKEN") or ""
    if not token:
        return False, None, "Meta token missing/expired — spend not live"
    return False, None, "Meta token env present but Insights pull not wired this seat"


def probe_ghl():
    if not (os.environ.get("GHL_API_KEY") or os.environ.get("GHL_PIT_TOKEN")):
        return False, "GHL token missing — calendars/leads not live"
    return False, "GHL token env present but calendar pull not wired this seat"


def speed_to_lead():
    if not SPEED_LOG.is_file() or SPEED_LOG.stat().st_size == 0:
        return {
            "value": None,
            "display": "RED — log missing",
            "target": "<60s",
            "as_of": None,
            "source": str(SPEED_LOG),
            "owner_kpi_type": "Shared",
            "status": "RED",
            "reason": "HARD FAIL: speed-to-lead log missing — never hardcoded 4.0/8.1",
        }
    # Real log present: parse last p50 if JSON lines with seconds.
    vals = []
    as_of = None
    for line in SPEED_LOG.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
            vals.append(float(row["seconds"]))
            as_of = row.get("ts") or as_of
        except Exception:
            continue
    if not vals:
        return {
            "value": None,
            "display": "RED — log unparseable",
            "target": "<60s",
            "as_of": None,
            "source": str(SPEED_LOG),
            "owner_kpi_type": "Shared",
            "status": "RED",
            "reason": "log exists but no parseable seconds",
        }
    vals.sort()
    p50 = vals[len(vals) // 2]
    return {
        "value": p50,
        "display": f"{p50:.1f}s",
        "target": "<60s",
        "as_of": as_of or now_iso(),
        "source": str(SPEED_LOG),
        "owner_kpi_type": "Shared",
        "status": "GREEN" if p50 < 60 else "RED",
        "reason": "live log",
    }


def kpi(value, display, target, as_of, source, owner, status, reason=""):
    return {
        "value": value,
        "display": display,
        "target": target,
        "as_of": as_of,
        "source": source,
        "owner_kpi_type": owner,
        "status": status,
        "reason": reason,
    }


def canary_kpi_reason():
    if not CANARY_RECEIPT.is_file():
        return "AMBER", "no canary receipt on disk — run false-green-canary.py"
    try:
        rec = json.loads(CANARY_RECEIPT.read_text())
    except Exception as e:
        return "RED", f"canary receipt unreadable: {type(e).__name__}"
    as_of = rec.get("as_of") or "missing as_of"
    passed = rec.get("pass") is True
    prod_intact = rec.get("production_snapshot_unchanged") is True
    if passed and prod_intact:
        return "GREEN", f"canary PASS as_of {as_of}; production snapshot not mutated"
    return "RED", f"canary FAIL as_of {as_of}; pass={rec.get('pass')} prod_intact={prod_intact}"


def main():
    out = resolve_out()
    qb_ok, realm, cash, qb_block = probe_qb()
    meta_ok, spend, meta_block = probe_meta()
    ghl_ok, ghl_block = probe_ghl()
    stl = speed_to_lead()

    blocked = not (qb_ok and meta_ok and ghl_ok)
    hist_cash_as_of = "2026-07-02"
    snap = {
        "schema": "fki.command-center-snapshot.v1",
        "command_center": "Function Command Center",
        "snapshot_date": now_iso(),
        "as_of": now_iso(),
        "status": "BLOCKED" if blocked else "LIVE",
        "flags": ["SAMPLE_FIXTURE_NOT_REAL"] if blocked else [],
        "qb_realm_id": realm or "UNAVAILABLE",
        "qb_realm_is_fki": bool(realm) and qb_ok,
        "blockers": [x for x in (qb_block, meta_block, ghl_block) if x],
        "madison_vercel_role": "FEED_ONLY",
        "vercel_url": "https://fki-dashboard.vercel.app",
        "daily_surface": "https://dashboard.franchiseki.com/bennett-cc/v3.html",
        "historical_labeled_not_live": {
            "cash_usd": 269,
            "liabilities_usd": 146527,
            "as_of": hist_cash_as_of,
            "source": "P0 Cash 392cf5514fd3810eac75c77cbcbe863f",
            "note": "Live QB NOT re-pulled. Do not treat as today.",
            "attribution_all_time_usd": 1130000,
            "attribution_as_of": "2026-04-25",
            "attribution_source": "34dcf5514fd3810bb0ecfea9fbbdb0d0",
        },
        "money_strip": {
            "cash": kpi(
                None if not qb_ok else cash,
                "BLOCKED" if not qb_ok else (f"${cash:,.0f}" if cash is not None else "BLOCKED"),
                "cover liabilities / payroll",
                None if not qb_ok else now_iso(),
                "QB FKI realm only",
                "Human-owned",
                "RED" if not qb_ok else "AMBER",
                qb_block or "",
            ),
            "pipeline_this_week_usd": kpi(
                105000,
                "$105k sitting (Courtney+Syed) — L10 labeled, not QB",
                "collect this week",
                "2026-08-17",
                "L10 Weekly 8/17 3bfcf5514fd381ce94dce96ae5bfd33e",
                "Shared",
                "AMBER",
                "meeting-labeled pipeline, not live CRM pull",
            ),
            "booked_calls": kpi(
                None,
                "BLOCKED",
                ">0 this week",
                None,
                "GHL calendars",
                "Agent-owned",
                "RED",
                ghl_block,
            ),
            "ad_spend": kpi(
                None,
                "BLOCKED",
                "$500/day cap (L10 8/17)",
                None,
                "Meta Insights",
                "Human-owned",
                "RED",
                meta_block,
            ),
            "bennett_gates": kpi(
                2,
                "Shaheen proposal sign + payroll late-fee",
                "0 open Bennett-only",
                "2026-08-17",
                "L10 8/17 commitments",
                "Human-owned",
                "RED",
                "Bennett gates only — not agent health chips",
            ),
        },
        "tiles": {
            "marketing": {
                "rocks": [
                    {"name": "IC CPL to $60 / IC ads live $50/day", "page": "34dcf5514fd3810bb0ecfea9fbbdb0d0", "owner": "George"},
                    {"name": "SH scale winning CBO", "page": "35fcf5514fd381998756d52a1383e9c5", "owner": "Brent/George"},
                    {"name": "FKI 2nd Opinion creative tests", "page": "34dcf5514fd3810bb0ecfea9fbbdb0d0", "owner": "George"},
                    {"name": "Daily social cadence", "page": "3bfcf5514fd381ce94dce96ae5bfd33e", "owner": "Christelle"},
                ],
                "kpis": [
                    kpi(None, "BLOCKED", "$60 CPL IC", None, "Meta+GHL", "Shared", "RED", meta_block),
                    kpi("1.41x", "1.41x SH Meta", ">1.0", "2026-04-25", "Attribution audit", "Shared", "RED", "as_of older than SLA"),
                    kpi(None, "BLOCKED spend vs $500/day cap", "$500/day", None, "Meta", "Human-owned", "RED", meta_block),
                    kpi(None, "BLOCKED tests this week", ">=1", None, "Meta ads manager", "Shared", "RED", meta_block),
                    kpi(None, "BLOCKED unpublished creatives", "0 stale", None, "Meta", "Shared", "RED", meta_block),
                ],
            },
            "appointment_setting": {
                "rocks": [
                    {"name": "Speed-to-lead under 60s on REAL clock", "page": "3aacf5514fd3812090b5dfdbfdc53ec9", "owner": "Cody"},
                    {"name": "3-touch reminder", "page": "3b4cf5514fd381c89ab4e589611e10ad", "owner": "Jenn"},
                    {"name": "No-show rebook + SH path live test", "page": "3b8cf5514fd381679c55e71cf7f3dff8", "owner": "Jenn"},
                ],
                "kpis": [
                    stl,
                    kpi(None, "BLOCKED unworked leads", "0", None, "GHL", "Agent-owned", "RED", ghl_block),
                    kpi(None, "BLOCKED booked", ">0", None, "GHL calendars", "Shared", "RED", ghl_block),
                    kpi(None, "BLOCKED show rate", ">50%", None, "GHL", "Shared", "RED", ghl_block),
                ],
            },
            "cold_lead_gen": {
                "rocks": [
                    {"name": "Broker outreach ($0 CAC historically)", "page": "34dcf5514fd381e1abdcff9683327c08", "owner": "Cody"},
                    {"name": "Broker handoff every unqualified SH lead", "page": "3bfcf5514fd381338c49df5e1a272159", "owner": "Cody"},
                    {"name": "Apollo/cold email health", "page": "360cf5514fd381a9ab97ed5136e88dab", "owner": "Kay"},
                    {"name": "Advaita inbound in CORRECT GHL account", "page": "3bacf5514fd3810fbc12dee7ed95c4be", "owner": "Jenn"},
                ],
                "kpis": [
                    kpi(None, "BLOCKED new conversations", ">0", None, "GHL/Apollo", "Shared", "RED", ghl_block),
                    kpi(None, "BLOCKED reply rate", ">5%", None, "Apollo", "Shared", "RED", "Apollo credits historically 0 (June 29)"),
                    kpi(None, "BLOCKED booked from outbound", ">0", None, "GHL", "Shared", "RED", ghl_block),
                    kpi(None, "BLOCKED Apollo credits", ">0", "2026-07-02", "P0 Cash", "Human-owned", "RED", "Apollo credits 0 as of July 2"),
                ],
            },
            "cro_sales": {
                "rocks": [
                    {"name": "ION Solar $5k collect", "page": "3c0cf5514fd38166b3ebe61f6bae4f68", "owner": "Madison/Kay"},
                    {"name": "Courtney Grant collect", "page": "3b8cf5514fd38167a38dfacd161c7184", "owner": "Madison"},
                    {"name": "Syed Ali $70k dated answer", "page": "3b8cf5514fd3814085cbc1e8159c3c8b", "owner": "Madison"},
                    {"name": "Neal/Cookie Cutters", "page": "39dcf5514fd381aa988bfb066e7f4339", "owner": "Bennett/Madison"},
                    {"name": "Anthony $3k/mo DROPPED 2026-08-13", "page": "381cf5514fd3814587aacac331a1c6f5", "owner": "—"},
                ],
                "kpis": [
                    kpi(105000, "$105k labeled this week", "collect", "2026-08-17", "L10 8/17", "Shared", "AMBER", "not live CRM"),
                    kpi(None, "BLOCKED close rate", ">20%", None, "GHL", "Shared", "RED", ghl_block),
                    kpi(None, "BLOCKED pre-call brief file counts", ">0", None, "Drive", "Agent-owned", "RED", "not counted this run"),
                    kpi(6000, "$6k still out after $1k collected", "0 AR this week", "2026-08-17", "L10 8/17", "Human-owned", "RED", "payroll missed 8/15"),
                ],
            },
            "ai_harness": {
                "rocks": [
                    {"name": "Double CORE money artifact daily", "page": "392cf5514fd381dbbb63c16a43de5b84", "owner": "Cameron/Mack"},
                    {"name": "Trail/routing actually bound", "page": "360cf5514fd381a9ab97ed5136e88dab", "owner": "Cameron"},
                    {"name": "One dashboard refresh cron", "page": "3aacf5514fd3812b8beeeecb782d2519", "owner": "Madison"},
                ],
                "kpis": [
                    kpi(None, "this write", "<24h", now_iso(), "snapshot writer", "Agent-owned", "GREEN", "writer ran"),
                    kpi(2, "2 designed canaries (STL log, QB expire)", "0 false-green", now_iso(), "false-green-canary-latest.json", "Agent-owned", *canary_kpi_reason()),
                    kpi(None, "BLOCKED token $ this week", "track", None, "provider invoices", "Human-owned", "RED", "not pulled"),
                    kpi(None, "imbalance visible on home", ">50% cycles money artifact", "2026-08-17", "180d contrast", "Shared", "RED", "L10: demand generated, paper not cash"),
                ],
            },
            "finance": {
                "rocks": [
                    {"name": "FKI QB realm re-auth", "page": "392cf5514fd3810eac75c77cbcbe863f", "owner": "Bennett/Kay"},
                    {"name": "Weekly P&L posted", "page": "360cf5514fd381f6aca0f88bb00b991a", "owner": "Kay"},
                    {"name": "Divvy real not SAMPLE", "page": "392cf5514fd3810eac75c77cbcbe863f", "owner": "Kay"},
                    {"name": "Subscriptions off Divvy before freeze", "page": "3bfcf5514fd381ce94dce96ae5bfd33e", "owner": "Kay"},
                ],
                "kpis": [
                    kpi(269, "$269 HISTORICAL", "cover payroll", hist_cash_as_of, "P0 Cash QB July 2", "Human-owned", "RED", "as_of older than SLA; live QB BLOCKED"),
                    kpi(None, "BLOCKED burn", "known", None, "QB FKI realm", "Human-owned", "RED", qb_block),
                    kpi(146527, "$146,527 HISTORICAL liabilities", "down", hist_cash_as_of, "P0 Cash", "Human-owned", "RED", "as_of July 2"),
                    kpi(None, "BLOCKED spend by brand", "by brand", None, "QB+Meta", "Shared", "RED", qb_block),
                    kpi(realm or "UNAVAILABLE", realm or "UNAVAILABLE", "print FKI realm", now_iso(), "writer", "Agent-owned", "RED" if not qb_ok else "GREEN", qb_block),
                ],
            },
        },
        "imbalance_180d": {
            "window": "2026-02-18..2026-08-18",
            "money_named": ["collections $105k", "ION $5k", "IC ads $50/day", "SH CBO", "payroll $6k out"],
            "harness_named": ["daily-sync AI prep", "Pulse/CC", "Calvin bot", "Trail/skills", "Vercel feed"],
            "read": "L10 8/17: generated demand, could not convert paper into cash. Daily surface was agent-first. Rebuild makes that visible.",
        },
        "bennett_gate_scan": {
            "open_gates": 2,
            "gate_list": ["Sign Shaheen proposal", "Payroll late-fee / collections"],
        },
        "next_3_actions": [
            "Collect Courtney + dated Syed answer ($105k)",
            "Re-auth FKI QB realm so cash is not July-2 history",
            "IC ads live $50/day — fastest franchise cash per Bennett 8/17",
        ],
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(snap, indent=2) + "\n")
    print(json.dumps({
        "wrote": str(out),
        "status": snap["status"],
        "qb_realm_id": snap["qb_realm_id"],
        "speed_to_lead": stl["status"],
        "flags": snap["flags"],
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
