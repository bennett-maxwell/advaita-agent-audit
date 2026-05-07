---
skill: revenue-drop-alert
pillar: monitoring
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI detects revenue problems in real time — Bennett never discovers revenue drop days later
---
# Revenue Drop Alert Skill v1

## Purpose
Immediate alert when QB revenue data shows anomalous drop vs. historical pattern. Bennett never discovers a revenue problem after the fact.

## Alert Thresholds

**CRITICAL (post immediately)**
- Day revenue < 50% of 7-day average → CRITICAL alert
- Zero revenue registered in QB for 2+ hours during business hours → CRITICAL alert

**WARNING (post within 1 hour)**
- Day revenue < 75% of 7-day average → WARNING alert
- MTD revenue > 15% below MTD goal at mid-month → WARNING alert

**INFORMATIONAL (include in daily standup)**
- Week revenue declining for 3rd consecutive week → informational flag
- MTD trending to miss goal by > 10% → informational flag

## Alert Format (Slack → #leo-auto)
```
🚨 REVENUE ALERT — [CRITICAL/WARNING]
Triggered: [timestamp MDT]
Current: [figure from QB — consult accountant for financial decisions]
Expected (7-day avg): [figure]
Variance: -X%
Possible causes: [AI-generated hypothesis based on pipeline data]
Recommended action: [specific next step]
```

## Context for Alert
AI includes pipeline context: "Pipeline shows [N] deals in final stages — revenue should normalize if [X] closes this week as expected."

Note: All revenue figures from QuickBooks API. For financial decisions, consult your accountant.

## Autonomy Value
**Replaces:** Weekly revenue review catching drops too late.
**Result:** Revenue anomalies detected within hours. Bennett has context and can act immediately.
**Advaita gap closed:** Financial monitoring — from 0% → 100% AI-autonomous.
