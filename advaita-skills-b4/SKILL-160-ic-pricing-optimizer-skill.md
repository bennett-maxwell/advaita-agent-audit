# SKILL-160: IC Pricing Optimizer
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Analyze IC coaching offer pricing vs market. Recommend optimal price points based on demand signals and competitor positioning.

## TRIGGER
Quarterly OR Bennett says "IC pricing review".

## EXECUTION STEPS
1. Pull current IC pricing tiers from Drive: `fki-ic/pricing.md`
2. Pull conversion data from GHL (last 90d): leads → booked → enrolled by tier
3. Pull revenue by tier from QB (last 90d)
4. Run Exa: pickleball coaching market pricing (comparable programs)
5. Calculate elasticity indicators:
   - Tier conversion rate (enrolled/leads)
   - Revenue per lead by tier
6. Generate pricing recommendation:
   - Price floor (below which quality perception drops)
   - Price ceiling (above which conversion drops sharply)
   - Optimal sweet spot (max revenue per lead)
7. Upload analysis to Drive: `fki-ic/pricing-analysis-[date].md`
8. Post to #leo-auto with recommendation

## DISCLAIMER
"Pricing recommendations are based on historical data and market research. Actual conversion rates will vary."

## DIAMOND GATE
- T1: Historical data only, no projections ✅
- T2: File > 200 bytes ✅
- T3: Recommendations only ✅
