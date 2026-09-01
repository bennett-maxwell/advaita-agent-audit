#!/usr/bin/env python3
"""False-green canaries: missing STL log → RED; expired QB → RED not $0.

Never writes the production snapshot. Writer --out / CC_SNAPSHOT_OUT goes to a temp dir.
Fails if writer rc != 0. Fails if production snapshot bytes change during the run.
Persists bennett-cc/false-green-canary-latest.json for the snapshot KPI bind.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
WRITER = HERE / "command-center-snapshot-writer.py"
PROD = HERE / "command-center-snapshot-latest.json"
RECEIPT = HERE / "false-green-canary-latest.json"


def sha256(path: Path):
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(env, out_path: Path):
    e = os.environ.copy()
    e.update(env)
    e["CC_SNAPSHOT_OUT"] = str(out_path)
    r = subprocess.run(
        [sys.executable, str(WRITER), "--out", str(out_path)],
        capture_output=True,
        text=True,
        env=e,
    )
    return r.returncode, r.stdout, r.stderr


def load_snap(path: Path):
    return json.loads(path.read_text())


def main():
    results = []
    prod_before = sha256(PROD)
    tmp = Path(tempfile.mkdtemp(prefix="cc-canary-"))
    missing = tmp / "no-such-speed-to-lead.log"
    out1 = tmp / "snap-missing-stl.json"
    out2 = tmp / "snap-expired-qb.json"

    rc, stdout, stderr = run({"CC_SPEED_TO_LEAD_LOG": str(missing)}, out1)
    if rc != 0:
        results.append((
            "missing_stl_log_is_RED_not_4.0",
            False,
            {"writer_rc": rc, "stdout": (stdout or "")[-400:], "stderr": (stderr or "")[-400:]},
        ))
    elif not out1.is_file():
        results.append(("missing_stl_log_is_RED_not_4.0", False, {"writer_rc": rc, "wrote": False}))
    else:
        snap = load_snap(out1)
        stl = snap["tiles"]["appointment_setting"]["kpis"][0]
        ok1 = stl.get("status") == "RED" and "4.0" not in str(stl.get("display")) and stl.get("value") is None
        results.append(("missing_stl_log_is_RED_not_4.0", ok1, stl))

    rc, stdout, stderr = run({
        "CC_SPEED_TO_LEAD_LOG": str(missing),
        "FKI_QB_REALM_ID": "",
        "QB_REALM_ID": "",
    }, out2)
    if rc != 0:
        results.append((
            "expired_qb_is_RED_not_zero",
            False,
            {"writer_rc": rc, "stdout": (stdout or "")[-400:], "stderr": (stderr or "")[-400:]},
        ))
    elif not out2.is_file():
        results.append(("expired_qb_is_RED_not_zero", False, {"writer_rc": rc, "wrote": False}))
    else:
        snap = load_snap(out2)
        cash = snap["money_strip"]["cash"]
        fin_cash = snap["tiles"]["finance"]["kpis"][0]
        ok2 = (
            snap["status"] == "BLOCKED"
            and "SAMPLE_FIXTURE_NOT_REAL" in snap["flags"]
            and cash["status"] == "RED"
            and cash["display"] == "BLOCKED"
            and cash["value"] is None
            and snap["qb_realm_id"] in ("UNAVAILABLE", "")
            and fin_cash["status"] == "RED"
        )
        results.append(("expired_qb_is_RED_not_zero", ok2, {"cash": cash, "qb_realm_id": snap["qb_realm_id"]}))

    prod_after = sha256(PROD)
    prod_intact = prod_before == prod_after
    if not prod_intact:
        results.append((
            "production_snapshot_unchanged",
            False,
            {"before": prod_before, "after": prod_after},
        ))
    else:
        results.append(("production_snapshot_unchanged", True, {"sha256": prod_after}))

    passed = all(p for _, p, _ in results)
    receipt = {
        "as_of": datetime.now(timezone.utc).isoformat(),
        "pass": passed,
        "production_snapshot_unchanged": prod_intact,
        "production_sha256": prod_after,
        "isolated_dir": str(tmp),
        "results": [{"name": n, "pass": p} for n, p, _ in results],
        "detail": [d for _, _, d in results],
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"results": receipt["results"], "pass": passed, "receipt": str(RECEIPT), "production_intact": prod_intact}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
