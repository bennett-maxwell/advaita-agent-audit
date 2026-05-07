---
skill: pipeline-stall-detection
pillar: monitoring
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI detects pipeline stalls before they become drops — proactive recovery vs. reactive mourning
---
# Pipeline Stall Detection Skill v1

## Purpose
Monitor every active candidate for velocity stalls and trigger recovery actions before the candidate drops. Real-time pipeline health vs. weekly snapshot.

## Stall Detection (continuous, runs every 4 hours)

For each active GHL candidate:
1. Calculate days in current stage
2. Compare to target benchmark (from skill-deal-velocity-tracking-v1)
3. Classify: ON TRACK / YELLOW FLAG / RED FLAG

**YELLOW FLAG** → AI auto-action:
- Generate broker Slack notification with specific recommended outreach
- Add to daily standup as priority item
- Create GHL task for broker with specific action + due date

**RED FLAG** → AI auto-action:
- Immediate Slack alert to broker (not just daily standup)
- Activate re-engagement trigger (skill-re-engagement-trigger-v1)
- Create P1 Sprint Board task
- If broker unresponsive after 24h → escalate to #leo-auto

## Top-of-Pipeline Stall (new leads not contacted)
Leads sitting in New Lead stage >24h without first contact → IMMEDIATE alert to broker
Leads sitting >72h → escalate to #leo-auto for assignment check

## Monthly Stall Pattern Analysis
If same stage consistently shows stalls → surface as conversion rate optimization opportunity (skill-conversion-rate-optimizer-v1).

## Autonomy Value
**Replaces:** Broker noticing stalled deals only at weekly pipeline review.
**Result:** Every stall detected within hours. Recovery actions triggered before candidate disengages completely.
**Advaita gap closed:** Pipeline health monitoring — from 0% → 100% AI-autonomous.
