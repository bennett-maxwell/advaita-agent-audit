# SKILL-114: SH Lead Qualification Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-qualify inbound Smash Hotel leads from all sources (Meta ads, organic, referrals). Score, tag, and route to appropriate funnel without manual review.

## TRIGGER
New GHL contact created with source tag sh-lead OR SH pipeline new entry.

## EXECUTION STEPS
1. Pull lead data: source, survey answers, UTM params
2. Score on 10-point IQ matrix:
   - Budget confirmed (3 pts)
   - Timeline < 90 days (2 pts)
   - Decision maker (2 pts)
   - Previous coaching exp (1 pt)
   - Social following > 5K (1 pt)
   - Referral source (1 pt)
3. Route by score:
   - 8-10: "hot" → book call immediately, notify Leo
   - 5-7: "warm" → 5-email nurture + retargeting tag
   - 1-4: "cold" → long-play nurture (90d drip)
4. Apply GHL tags: sh-hot | sh-warm | sh-cold + IQ score
5. Post daily digest to #leo-auto: new leads by tier

## DIAMOND GATE
- T1: No qualification guarantees ✅
- T2: File > 200 bytes ✅
- T3: Tag writes REVERSIBLE ✅
