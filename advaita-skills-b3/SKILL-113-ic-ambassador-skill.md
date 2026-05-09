# SKILL-113: IC Ambassador Program Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Manage IC brand ambassador pipeline. Identify top alumni, activate referral tracking, automate commission payouts.

## TRIGGER
Monthly 1st (auto) OR GHL tag event: ic-graduate.

## EXECUTION STEPS
1. Pull ic-graduate contacts from last 60d
2. Score by: testimonial strength, social following, referral history
3. Top 10: send Ambassador invitation email with affiliate link (ThriveCart)
4. Track referrals via UTM + ThriveCart affiliate dashboard
5. Monthly: generate commission report from ThriveCart API
6. QB draft entry for affiliate payouts (NOT posted — finance review required)
7. Post ambassador pipeline summary to #leo-auto

## DIAMOND GATE
- T1: No income claims for ambassador earnings ✅
- T2: File > 200 bytes ✅
- T3: QB payout draft (not posted) — finance review gate ✅
