---
skill: closing-signal-detection
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI detects when candidate is ready to close — broker gets real-time "close now" alerts
---
# Closing Signal Detection Skill v1

## Purpose
AI monitors all candidate touchpoints for closing signals and immediately alerts broker with a "CLOSE NOW" notification when signals align.

## Primary Closing Signals

**Verbal/Written Signals** (detected in email or call notes):
- "When can I start?" / "What's the next step to move forward?"
- "I've talked to my spouse and we're aligned"
- "I've spoken to my attorney and we're good"
- "Funding is in place" / "I have the capital ready"
- "I've done my validation calls and I'm impressed"
- Questions about territory award process, training dates, opening timelines

**Behavioral Signals** (GHL activity data):
- FDD downloaded + last reviewed <7 days ago
- Visited FKI "get started" or pricing pages in last 48h
- Opened 3+ emails in last 7 days
- Scheduled a call proactively (not prompted)
- Completed all validation calls in rapid succession

**Pipeline Stage Signals**:
- All 5 readiness criteria met (buyer-readiness-assessment-v1)
- Validation calls completed + positive feedback noted
- Funding path confirmed in GHL

## CLOSE NOW Alert Format (Slack → broker)
```
🚨 CLOSE NOW SIGNAL — [Candidate Name]
Signals detected: [list of specific signals]
Last contact: [X days ago]
Recommended action: Call today. Agenda: territory selection + award timeline.
```

## Autonomy Value
**Replaces:** Broker manually checking if each candidate is ready.
**Result:** Broker always calls at peak intent moment. Conversion rate maximized.
**Advaita gap closed:** Close timing intelligence — from 0% → 95% AI-autonomous.
