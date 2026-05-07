---
skill: post-call-debrief
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI captures call insights and updates pipeline — replaces broker manual CRM notes
---
# Post-Call Debrief Skill v1

## Purpose
Within 15 minutes of a discovery call ending, AI auto-generates a structured debrief and updates GHL without broker data entry.

## Trigger
Calendar event marked as completed + broker post-call voice memo OR broker sends "debrief [candidate name]" to Squirrel.

## Debrief Structure (auto-generated)

**Call Summary** (2–3 sentences): What was discussed, where candidate stands, what changed.

**Key Findings**:
- Capital situation update (if new info)
- Timeline update (if changed)
- Brand reactions (positive / negative / neutral for each brand discussed)
- Objections raised + how handled
- Spouse/partner status update

**Readiness Assessment Update**: Re-run buyer-readiness-assessment-v1 with new data.

**Recommended Next Actions** (AI-generated, 3 max):
1. Specific follow-up email/action within 24h
2. Resource to send candidate
3. Next milestone to schedule

**GHL Updates** (AI executes automatically — REVERSIBLE):
- Stage update (if warranted)
- Tags update
- Note field: structured debrief summary
- Task creation: next follow-up action with due date

## Autonomy Value
**Replaces:** Broker spending 10–20 min after every call updating CRM.
**Result:** AI does 100% of post-call admin. Broker spends 100% of time on calls.
**Advaita gap closed:** Post-call admin — from 0% → 100% AI-autonomous.
