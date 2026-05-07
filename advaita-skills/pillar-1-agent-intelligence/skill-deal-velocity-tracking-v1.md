---
skill: deal-velocity-tracking
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI monitors pipeline velocity — replaces manual pipeline review meetings
---
# Deal Velocity Tracking Skill v1

## Purpose
AI continuously monitors how fast each candidate is moving through the pipeline and flags stalls before they become drops.

## Velocity Benchmarks (target days per stage)

| Stage | Target Days | Yellow Flag | Red Flag |
|-------|-------------|-------------|----------|
| New Lead → First Contact | ≤1 | 2 days | 3+ days |
| First Contact → Discovery Scheduled | ≤5 | 7 days | 10+ days |
| Discovery → FDD Requested | ≤7 | 14 days | 21+ days |
| FDD Requested → Validation Calls | ≤14 | 21 days | 30+ days |
| Validation → Award Decision | ≤21 | 30 days | 45+ days |
| Total Pipeline (intro to close) | ≤60 days | 75 days | 90+ days |

## Automated Monitoring Actions

**Yellow Flag** → AI sends broker Slack notification: "[Candidate name] is slowing in [stage]. Last contact: [X days ago]. Suggested action: [specific outreach]"

**Red Flag** → AI creates high-priority task in GHL + Slack alert to broker + #leo-auto notification.

**Stall Recovery Sequence** → AI triggers appropriate re-engagement based on last known objection or hesitation.

## Pipeline Velocity Report (daily, 8 AM MDT)
Posted to #leo-auto:
- Active candidates by stage
- Candidates hitting yellow/red flag today
- Deals closed in last 7 days
- Pipeline value and probability-weighted close forecast

## Autonomy Value
**Replaces:** Weekly pipeline review meeting where broker manually reviews all active candidates.
**Result:** Proactive intervention at exact right moment. Zero stalls missed.
**Advaita gap closed:** Pipeline monitoring — from 0% → 100% AI-autonomous.
