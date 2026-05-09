# SKILL-173: Franchise Resale Value Estimator
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Estimate resale value of SRP franchise units for transfer pricing. Market-based methodology.

## TRIGGER
Franchisee inquires about transfer/resale OR annually for portfolio visibility.

## EXECUTION STEPS
1. Pull franchisee financial data: trailing 12m revenue, EBITDA estimate
2. Load industry multiple benchmarks from Drive: `fki-franchise/valuation-benchmarks.md`
3. Apply sports retail franchise valuation methodology:
   - Revenue multiple range (from industry data)
   - EBITDA multiple range
   - Lease value adjustment
   - Brand premium/discount factor
4. Generate valuation range (not a precise number — range only)
5. MANDATORY disclaimer: "This is an estimate only for internal planning purposes. Actual sale price depends on buyer negotiations, due diligence, and market conditions at time of sale. This is not a representation of franchise system earnings."
6. Upload to Drive: `fki-franchise/valuations/[franchisee-id]-[date].md`
7. Post to #leo-auto: franchisee ID + estimated range (no $ in Slack)

## DIAMOND GATE
- T1: Estimate only. Not an earnings representation. FDD compliance ✅
- T2: File > 200 bytes ✅
- T3: Valuation document — no transaction commitment ✅
