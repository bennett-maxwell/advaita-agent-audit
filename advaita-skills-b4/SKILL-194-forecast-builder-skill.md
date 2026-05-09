# SKILL-194: Revenue Forecast Builder
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Build FKI quarterly revenue forecasts from actuals + pipeline. Planning tool for Bennett, NOT a guarantee.

## TRIGGER
Quarterly (March/June/Sep/Dec 1st) OR Bennett says "build forecast [quarter]".

## EXECUTION STEPS
1. Pull QB actuals: last 12 months by brand/offer
2. Pull GHL pipeline: active deals by stage × close probability
3. Pull Meta/Google pipeline: campaign ROAS × projected spend
4. Build 3-scenario forecast:
   - Conservative: trailing 90d run rate only
   - Base: trailing 90d + 50% of hot pipeline
   - Optimistic: trailing 90d + 80% of hot + medium pipeline
5. Break down by brand: IC / SH / SRP
6. MANDATORY disclaimer: "This is a planning projection based on historical data and current pipeline. It is not a guarantee or prediction of future revenue. Actual results will depend on market conditions, execution, and factors outside FKI's control."
7. Upload to Drive: `fki-finance/forecasts/[quarter]-[year]-forecast.md`
8. Post 3-scenario summary to #leo-auto (% growth vs prior quarter)

## DIAMOND GATE
- T1: Planning disclaimer mandatory. Scenarios labeled clearly ✅
- T2: File > 200 bytes ✅
- T3: Projection document — no budget commitments ✅
