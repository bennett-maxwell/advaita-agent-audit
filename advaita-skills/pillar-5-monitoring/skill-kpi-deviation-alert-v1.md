---
skill: kpi-deviation-alert
pillar: monitoring
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI detects KPI deviations in real time — problems surface in hours, not months
---
# KPI Deviation Alert Skill v1

## Purpose
Monitor all FKI KPIs against targets and trigger alerts when deviations exceed thresholds. AI is the first to know when something is wrong — always before Bennett notices manually.

## KPI Dashboard (monitored continuously)

| KPI | Source | Alert Threshold |
|-----|--------|----------------|
| Lead volume (weekly) | GHL | <70% of weekly target |
| CPL (cost per lead) | Meta Ads | >140% of CPL target |
| Discovery call show rate | GHL/Calendar | <70% of scheduled |
| FDD to validation conversion | GHL stages | <50% of FDD stage |
| Pipeline velocity (avg days in stage) | GHL | Any stage >130% of target |
| Close rate (30-day rolling) | GHL | <30% of qualified leads |
| Revenue per week | QB | <75% of weekly target (consult accountant; QB-verified) |

## Alert Format (Slack #leo-auto)
```
📊 KPI DEVIATION ALERT
Metric: [KPI name]
Current: [actual value]
Target: [target value]
Deviation: [X% below/above target]
Duration: [how long this has been off target]
Hypothesis: [AI assessment of likely cause]
Recommended action: [specific next step]
```

## Escalation
If KPI alert unresolved after 3 days → escalate to weekly business review as P1 item.

## Autonomy Value
**Replaces:** Monthly performance review catching problems after the fact.
**Result:** KPI problems detected within days. Root cause identified. Action recommended. Business always self-correcting.
**Advaita gap closed:** KPI health monitoring — from 0% → 100% AI-autonomous.
