# SKILL-132: Revenue Attribution Automation
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Attribute FKI revenue to source (Meta ads, organic, referral, repeat). Multi-touch attribution model from GHL UTMs + QB.

## TRIGGER
Weekly Sunday 11 PM MDT (auto) OR Bennett says "attribution report".

## EXECUTION STEPS
1. Pull QuickBooks: all payments last 7d (name, amount, date)
2. Cross-reference with GHL: contact source UTM, first touch, last touch
3. Assign attribution:
   - First-touch: original lead source
   - Last-touch: final channel before purchase
   - Linear: equal credit across all touches
4. Build attribution table by channel:
   - Meta Ads (campaign-level)
   - Google Ads
   - Organic (SEO/Social)
   - Referral (source name)
   - Direct
5. Calculate: revenue per channel, CAC per channel, ROAS per channel
6. Upload to Drive: `fki-reports/attribution-[date].md`
7. Post weekly summary to #leo-auto

## DIAMOND GATE
- T1: Actuals only — no projections ✅
- T2: File > 200 bytes ✅
- T3: Read-only ✅
