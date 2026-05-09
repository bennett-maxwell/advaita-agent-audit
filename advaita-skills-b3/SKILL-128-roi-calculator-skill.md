# SKILL-128: ROI Calculator Automation
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Generate real-time ROI calculations for FKI ad spend, coaching programs, and franchise investments. Pulls from QB + Meta Ads API.

## TRIGGER
Bennett says "ROI [brand] [period]" OR weekly Monday digest.

## EXECUTION STEPS
1. Pull from QuickBooks API:
   - Revenue by brand/offer for period
   - COGS
   - Gross profit
2. Pull from Meta Ads API:
   - Total ad spend for period by brand
   - Attributed conversions (pixel events)
3. Calculate:
   - Blended ROAS = Revenue / Total Ad Spend
   - CAC = Total Ad Spend / New Clients
   - LTV:CAC ratio
   - Gross margin %
   - Payback period (months to recover CAC)
4. Generate ROI summary table
5. Flag: ROAS < 1.5x → alert. LTV:CAC < 3:1 → alert.
6. Upload to Drive: `fki-reports/roi-[brand]-[period].md`
7. Post to #leo-auto

## DISCLAIMER
All figures are historical actuals from connected APIs. Not a projection of future results.

## DIAMOND GATE
- T1: Historical actuals only — no forward projections ✅
- T2: File > 200 bytes ✅
- T3: Read-only calculations ✅
