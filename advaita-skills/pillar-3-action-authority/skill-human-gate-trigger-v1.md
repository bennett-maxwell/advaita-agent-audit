---
skill: human-gate-trigger
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI knows exactly when to stop and escalate — removes all gray-area guessing
---
# Human Gate Trigger Skill v1

## Purpose
Define the exact conditions under which AI must stop and wait for Bennett. Clear triggers prevent both over-escalation (slows autonomy) and under-escalation (creates risk).

## Human Gate Triggers (HARD — no exceptions)

**BIOMETRIC**: Any action requiring physical identity verification, signatures in person, or biometric authentication.

**LEGAL**: External contract review, franchise agreement execution, legal filings, any action with attorney-client privilege implications.

**FINANCIAL THRESHOLD**: Any transaction, commitment, or authorization exceeding the threshold set in Bennett's authorization scope (currently: any irreversible financial action above the authorized limit). See proactive autonomy skill for current threshold. Consult Bennett for any ambiguous financial commitment.

**EXTERNAL IDENTITY**: Communications on behalf of Bennett to external parties where Bennett's personal identity or reputation is at stake.

**IRREVERSIBLE with >24h impact**: Any action that cannot be reversed within 24 hours and has significant business impact.

## Near-Gate Situations (AI uses judgment, may escalate)
- Novel situation with no prior skill protocol
- Conflicting signals from multiple data sources
- Legal area outside AI's documented knowledge
- Emotional/relationship complexity beyond AI capability

## Human Gate Escalation Protocol
1. STOP execution
2. Document: what the action is, why it requires human gate, what information is needed from Bennett
3. Post to #leo-auto: "@Leo — HUMAN GATE REQUIRED. Details: [summary]. Waiting for Bennett decision."
4. Log to Sprint Board with status BLOCKED
5. DO NOT attempt workaround or proceed without Bennett response

## Anti-Pattern: Fake Human Gate
AI must NOT fabricate a human gate requirement to avoid executing something within its capability. Human gate is for genuine blockers only. Unnecessary human gates slow autonomy.

## Autonomy Value
**Replaces:** AI either doing too much (taking actions it shouldn't) or too little (escalating trivial things).
**Result:** Precisely calibrated autonomy. Bennett only involved for things that genuinely require him.
**Advaita gap closed:** Escalation calibration — from 0% → 100% properly defined.
