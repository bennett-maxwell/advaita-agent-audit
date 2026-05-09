# SKILL-109: Audience Segmentation Automation
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-segment FKI GHL contacts into ICPs, buyer stages, and re-engagement tiers. Updates contact tags. Feeds campaign targeting.

## TRIGGER
Weekly Sunday 11 PM MDT (auto) OR Bennett says "segment [brand] contacts".

## EXECUTION STEPS
1. Pull GHL contact list for brand (last 90d active)
2. Score each contact on:
   - Engagement score (email opens, link clicks, SMS replies)
   - Pipeline stage (lead / booked / enrolled / churned)
   - LTV (from QB sync)
   - Days since last touch
3. Apply segment tags:
   - hot-lead: score > 80 + stage = lead
   - warm-nurture: score 40-80
   - re-engage: score < 40 + last touch > 30d
   - vip: LTV > $5,000
   - churn-risk: enrolled + no login > 21d
4. Update GHL contact tags via API
5. Export segment counts to Drive: `fki-reports/segmentation-[date].md`
6. Post segment summary to #leo-auto

## DIAMOND GATE
- T1: No claims about segment performance ✅
- T2: File > 200 bytes ✅
- T3: Tag writes REVERSIBLE (can untag) ✅
