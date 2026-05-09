# SKILL-116: SH Client Success Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Proactive client success monitoring for Smash Hotel enrolled clients. Flags risk, surfaces wins, triggers milestone celebrations.

## TRIGGER
Weekly Tuesday 8 AM MDT (auto).

## EXECUTION STEPS
1. Pull SH enrolled clients from GHL (tag: sh-enrolled)
2. Score weekly health:
   - Session attendance
   - Revenue milestone hits (from QB sync)
   - NPS pulse (email survey auto-triggered at 30/60/90d)
3. Flag: NPS < 7 OR milestone overdue by > 14d
4. For flags: trigger personal check-in email from Bennett (template in Drive)
5. For milestones hit: trigger celebration email + testimonial ask
6. Log health scores to Drive: `fki-reports/sh-client-health-[date].md`
7. Post weekly summary to #leo-auto

## DIAMOND GATE
- T1: No revenue projections in client comms ✅
- T2: File > 200 bytes ✅
- T3: Emails queued (not sent) pending Leo activation ✅
