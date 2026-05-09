# SKILL-166: Franchisee Performance Ranking
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Monthly objective ranking of SRP franchisees by performance. Identifies top performers for recognition, bottom performers for support.

## TRIGGER
Monthly 1st (auto).

## EXECUTION STEPS
1. Pull franchisee roster from Drive
2. Pull per-franchisee metrics:
   - Gross revenue (QB or franchisee-reported)
   - Royalty payments current? (from SKILL-136)
   - Training compliance (from SKILL-158)
   - Customer reviews (Google/Yelp aggregate)
   - Vendor compliance (from SKILL-159)
3. Composite score (1-100):
   - Revenue performance: 40%
   - Compliance: 30%
   - Customer satisfaction: 20%
   - Financial: 10%
4. Rank all franchisees
5. Top 3: trigger recognition email from Bennett
6. Bottom 3: trigger support check-in + remediation plan template
7. Upload ranking to Drive: `fki-franchise/rankings-[month]-[year].md`
8. Post to #leo-auto (aggregate stats, no individual names in Slack)

## DIAMOND GATE
- T1: Objective metrics only. No revenue projections ✅
- T2: File > 200 bytes ✅
- T3: Recognition/support emails queued not sent ✅
