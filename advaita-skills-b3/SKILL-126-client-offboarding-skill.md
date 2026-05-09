# SKILL-126: Client Offboarding Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Handle churned or graduating clients gracefully. Protect brand reputation, collect NPS, trigger win-back when appropriate.

## TRIGGER
GHL stage: churned OR program-complete.

## EXECUTION STEPS
1. Determine exit type: natural graduation vs churn
2. For GRADUATION:
   - Send certificate + celebration email
   - Trigger testimonial request (SKILL-122)
   - Offer alumni community invite
   - Add to cross-brand upsell pipeline (SKILL-121)
3. For CHURN:
   - Send exit survey (2-question NPS)
   - Wait 30d, then trigger win-back sequence (3-email)
   - Flag in GHL: churn-[reason] tag
4. Both: update QB contact status
5. Log offboarding event to Drive: `fki-ops/offboarding-log-[date].md`
6. Post weekly churn report to #leo-auto

## DIAMOND GATE
- T1: No outcome claims in exit comms ✅
- T2: File > 200 bytes ✅
- T3: Win-back queued not sent ✅
