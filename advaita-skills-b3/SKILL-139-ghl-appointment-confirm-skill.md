# SKILL-139: GHL Appointment Confirmation Automation
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Automated appointment confirmation, reminder, and no-show recovery for all FKI scheduled calls.

## TRIGGER
GHL calendar: appointment booked (any brand).

## EXECUTION STEPS
1. On booking:
   - Send confirmation email + SMS immediately
   - Add to GHL pipeline: booked
2. 24h before: send reminder email + SMS with Zoom link
3. 1h before: SMS reminder (name + time + link)
4. 15 min after scheduled time: if no GHL note added, trigger no-show sequence:
   - Immediate SMS: "Hey [name], missed you — want to reschedule?"
   - 1h: reschedule email with link
   - 24h: final reschedule attempt
5. If reschedule booked: reset confirmation sequence
6. Log no-show rate to Drive: `fki-reports/noshow-log-[month].md`
7. Post weekly no-show rate to #leo-auto

## DIAMOND GATE
- T1: No outcome claims in confirmation copy ✅
- T2: File > 200 bytes ✅
- T3: SMS/email sequences REVERSIBLE (can cancel) ✅
