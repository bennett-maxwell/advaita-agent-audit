# SKILL-143: GHL SMS Compliance Monitor
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Ensure all FKI SMS sends comply with TCPA. Monitor opt-out rates, scrub lists, flag compliance issues before sends.

## TRIGGER
Before every SMS broadcast. Weekly compliance audit (Sunday 9 PM MDT).

## EXECUTION STEPS
PRE-SEND CHECK:
1. Verify all contacts in send list have sms-consent=true tag in GHL
2. Verify send time: 8 AM - 8 PM recipient local time
3. Verify message contains STOP opt-out language
4. Block send if any check fails — alert Leo

WEEKLY AUDIT:
1. Pull GHL opt-outs last 7d
2. Calculate opt-out rate % (flag if > 2%)
3. Verify opted-out contacts are removed from all active sequences
4. Log compliance report to Drive: `fki-compliance/sms-audit-[date].md`
5. Post audit summary to #leo-auto

## DIAMOND GATE
- T1: TCPA compliance enforced ✅
- T2: File > 200 bytes ✅
- T3: Audit + block REVERSIBLE ✅
