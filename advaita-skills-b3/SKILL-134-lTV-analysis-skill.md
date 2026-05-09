# SKILL-134: LTV Analysis Automation
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Calculate and track customer lifetime value by brand, cohort, and acquisition source. Foundation for ROAS targets and ad budgets.

## TRIGGER
Monthly 1st (auto) OR Bennett says "LTV analysis".

## EXECUTION STEPS
1. Pull QuickBooks: all transactions per contact (last 24 months)
2. Segment by: brand, cohort (enrollment month), acquisition source
3. Calculate per segment:
   - Average purchase value
   - Purchase frequency
   - Average customer lifespan (months)
   - LTV = Avg Value × Frequency × Lifespan
4. Cohort analysis: month-by-month retention curves
5. LTV by acquisition source (Meta vs organic vs referral)
6. Update CPA targets in Drive based on LTV changes
7. Upload to Drive: `fki-finance/ltv-analysis-[month]-[year].md`
8. Post key LTV changes (>10% swing) to #leo-auto

## DIAMOND GATE
- T1: Historical data only — LTV is backward-looking ✅
- T2: File > 200 bytes ✅
- T3: Read-only analysis ✅
