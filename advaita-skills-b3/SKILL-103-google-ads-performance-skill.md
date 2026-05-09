# SKILL-103: Google Ads Performance Automation
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Automated Google Ads monitoring and bid adjustment for FKI brands. Daily pull + keyword-level optimization recommendations.

## TRIGGER
Daily 7:30 AM MDT OR Bennett says "google ads report".

## EXECUTION STEPS
1. Pull Google Ads API data for all FKI accounts (last 7d):
   - Impressions, clicks, conversions, cost
   - Keyword-level Quality Score
   - Search impression share
2. Flag: keywords with CPA > 2x target AND impressions > 100
3. Flag: keywords with Quality Score < 5
4. Recommend: pause low-QS keywords, increase bids on top converters
5. REVERSIBLE recommendations only — no auto-bid changes
6. Post recommendations to #leo-auto for Leo to execute
7. Log report to Drive: `fki-reports/google-ads-daily-[date].md`

## DIAMOND GATE
- T1: No income projections ✅
- T2: File > 200 bytes ✅
- T3: Report only — no auto-bid execution (Leo executes after review) ✅
