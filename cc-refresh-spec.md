> ## ⛔ GATED 2026-08-04 — READ BEFORE IMPLEMENTING THIS CRON
> Company financial figures were **removed from this public repo** on 2026-08-04 by decision of
> Madison Lanz (Operations Manager). `dashboard.franchiseki.com` is a **public** GitHub Pages site
> served from the **public** repo `bennett-maxwell/advaita-agent-audit`, so anything written here is
> world-readable.
>
> **Do NOT restore the finance sed-replace steps below until the company-only access gate is live**
> (runbook: `fki-dashboard/docs/COMPANY-ONLY-ACCESS-RUNBOOK.md`).
>
> The old `"$390K"` sed anchors **no longer exist** — `hub/index.html`, `finance-hub/index.html`,
> `personal-finance/index.html` and `cc-data-snapshot.json` now render/where applicable a `🔒 gated`
> placeholder. A sed-replace keyed on the old anchor will silently no-op. Operational metrics
> (leads, autonomy, CPL, funnel, machine RAM) are unchanged and still safe to refresh.

# CC Daily Refresh Script Spec
# For Leo to implement as daily 6AM cron on Ivan
# Generated: 2026-05-26 by Helix sub-agent

## Purpose
Update all CC data sources daily so Bennett never needs to login to external systems.
Every number on every CC page comes from a live data pull — never from memory.

## Script: cc-daily-refresh.sh
Location on Ivan: ~/.openclaw/scripts/cc-daily-refresh.sh
Cron: 0 6 * * * ~/.openclaw/scripts/cc-daily-refresh.sh >> ~/.openclaw/logs/cc-refresh.log 2>&1

---

## Step 1: QB Financial Data
Source: Ivan SSH → fred-bookkeeper cron output
```bash
SSH openclaw@100.103.51.12 'cat ~/.openclaw/workspace/finance/latest-snapshot.json'
```
Update targets:
- cc-data-snapshot.json → fki_financials section (ytd_revenue, ytd_net, gross_margin_pct, monthly_run_rate)
- finance-hub/index.html → YTD/net/margin KPI cells (grep for "$390K" anchor, sed replace)
- hub/index.html → KPI strip YTD Revenue cell + Finance CC card metric

Gate: If fred snapshot is >24h old, flag in cc-data-snapshot.json with "stale": true

---

## Step 2: GHL Pipeline Data (when PIT token valid)
Source: Ivan SSH → piper-pipeline cron output
```bash
SSH openclaw@100.103.51.12 'cat ~/.openclaw/workspace/pipeline-latest.json'
```
Update targets:
- cc-data-snapshot.json → sales_pipeline section (total_active_leads, stage_1..4, stale_leads_14d)
- hub/index.html → KPI strip "Active Leads" cell
- hub/index.html → Sales Pipeline CC card metric

Token gate: If GHL returns 401, write note="GHL 401 — Kay must refresh PIT token" and set all
pipeline values to null. Display "GHL 401" in hub KPI strip (already set as fallback).

---

## Step 3: Meta Ads Data (when FB token valid)
Source: Ivan SSH → meta-ads snapshot
```bash
SSH openclaw@100.103.51.12 'cat ~/.openclaw/workspace/meta-ads-latest.json'
```
Update targets:
- marketing/marketing-data.json → all fields
- cc-data-snapshot.json → marketing section (meta_30d_spend, meta_30d_leads, meta_cpl, meta_roas)
- marketing/index.html → Ad Performance tab data cells

Token gate: If FB token returns 401, set fb_token_status="expired — Bennett must refresh" and
preserve last known spend/CPL values with "stale": true flag.

---

## Step 4: Machine Health
Source: Ivan SSH → machine-health-collector.sh
```bash
SSH openclaw@100.103.51.12 '~/.openclaw/scripts/machine-health-collector.sh'
```
Update targets:
- hub/machine-health.json → full output
- cc-data-snapshot.json → agent_health section (tiffany/ivan/mack status)
- hub/index.html → Machine RAM KPI cell

---

## Step 5: Human Gates Count
Source: cc-data-snapshot.json human_gates array (maintained by Mack)
Logic: count entries where urgency != "RESOLVED"
Update targets:
- cc-data-snapshot.json → agent_health.open_bennett_gates
- hub/index.html → Human Gates banner count badge (grep "7 open", replace with live count)
- hub/index.html → Human Gates CC card metric

---

## Step 6: Advaita Score
Source: Ivan SSH → autonomy score from last Overdrive run
```bash
SSH openclaw@100.103.51.12 'cat ~/.openclaw/workspace/latest-autonomy-score.json'
```
Update targets:
- cc-data-snapshot.json → agent_health.autonomy_score_pct
- hub/index.html → KPI strip Autonomy cell
- hub/index.html → Advaita Deploy CC card metric

---

## Step 7: Update Snapshot Timestamp
```bash
# Patch snapshot_date in cc-data-snapshot.json
SNAPSHOT_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
jq --arg d "$SNAPSHOT_DATE" '.snapshot_date = $d' cc-data-snapshot.json > /tmp/cc-snap.json && mv /tmp/cc-snap.json cc-data-snapshot.json
```

---

## Step 8: Git Push
```bash
cd /path/to/advaita-agent-audit
git add cc-data-snapshot.json hub/index.html finance-hub/index.html marketing/marketing-data.json hub/machine-health.json
git commit -m "chore: CC daily refresh $(date +%Y-%m-%d)"
git push origin main
```

---

## Step 9: Slack Receipt
```bash
# Post to #leo-auto
curl -X POST https://slack.com/api/chat.postMessage \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"channel\":\"#leo-auto\",\"text\":\"CC DAILY REFRESH COMPLETE $(date +%Y-%m-%d) — QB $ytd_rev YTD · GHL $pipeline_status · Meta $meta_status · $(date -u +%H:%M)Z\"}"
```

---

## Blocked Gates (require human action before automation works)

| Gate | Blocker | Urgency |
|------|---------|---------|
| GHL pipeline live data | Kay must refresh PIT token (GHL 401) | HIGH |
| Meta Ads ROAS data | Bennett must refresh FB token | HIGH |
| Rachel property alerts | Bennett must add ~4 property records | LOW |

---

## Data Flow Diagram

```
QB (Ivan fred cron)        → latest-snapshot.json → finance-hub/ + hub/ + cc-data-snapshot.json
GHL (piper cron, PIT gate) → pipeline-latest.json → hub/ KPI strip + cc-data-snapshot.json
Meta (FB token gate)       → meta-ads-latest.json → marketing/ + cc-data-snapshot.json
Machine health (Ivan SSH)  → machine-health.json  → hub/ + cc-data-snapshot.json
Advaita score (Overdrive)  → autonomy-score.json  → hub/ + cc-data-snapshot.json
                                                     ↓
                                              git push → GitHub Pages → dashboard.franchiseki.com
```

## WO to Leo
To implement: "Leo — implement cc-daily-refresh.sh on Ivan per spec at:
/Users/temp/Projects/advaita-agent-audit/cc-refresh-spec.md
Cron: 0 6 * * * daily. All data sources documented. 2 gates blocked pending token refresh (GHL+Meta)."
