# SKILL-130: Break-Even Analyzer
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Calculate break-even point for new FKI offers, campaigns, or investments. Instant analysis without financial analyst.

## TRIGGER
Bennett says "break even on [offer/investment]" OR new offer launch planning.

## EXECUTION STEPS
1. Collect inputs:
   - Fixed costs (monthly overhead allocated to offer)
   - Variable cost per unit/client
   - Price point
   - Projected conversion rate
2. Calculate:
   - Break-even units = Fixed Costs / (Price - Variable Cost)
   - Break-even revenue
   - Break-even timeline (at current conversion rate)
   - Margin of safety %
3. Sensitivity analysis: 3 scenarios (pessimistic / base / optimistic)
4. Format as decision brief
5. Upload to Drive: `fki-finance/break-even-[offer]-[date].md`
6. Post to #leo-auto

## DISCLAIMER
"These are estimates based on inputs provided. Actual results will vary."

## DIAMOND GATE
- T1: Estimates labeled as estimates ✅
- T2: File > 200 bytes ✅
- T3: Modeling only — no financial commitments ✅
