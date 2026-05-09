# SKILL-106: SMS Broadcast Automation
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE (draft only)

## PURPOSE
Draft and queue SMS broadcasts for FKI lead lists in GHL. Handles opt-in compliance, timing windows, and personalization tokens.

## TRIGGER
Bennett says "SMS blast [brand] [message]" OR autopilot detects webinar registration window open.

## EXECUTION STEPS
1. Load GHL contact segment from Drive config (opted-in only)
2. Run bennett-intelligence-layer-skill for message framing
3. Draft SMS (160 char limit, include STOP opt-out)
4. Compliance check: only send 8 AM - 8 PM recipient local time
5. Create GHL broadcast in DRAFT state (not sent)
6. Post draft preview to #leo-auto for Leo to activate
7. Log: draft ID, segment size, send window

## COMPLIANCE RULES
- Always include "Reply STOP to unsubscribe"
- Never send between 8 PM and 8 AM recipient local time
- Segment must be opted-in only (GHL tag: sms-consent=true)

## DIAMOND GATE
- T1: No income claims in SMS. Opt-out language required ✅
- T2: File > 200 bytes ✅
- T3: Draft state only — Leo must activate ✅
