# SKILL-189: Attribution Model Tuner
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Continuously refine FKI revenue attribution model as new data arrives. Improve accuracy of CAC and ROAS calculations.

## TRIGGER
Monthly (after SKILL-132 revenue attribution run).

## EXECUTION STEPS
1. Pull last 90d attribution data (SKILL-132 output)
2. Compare attribution models:
   - First-touch
   - Last-touch
   - Linear (equal weight)
   - Time-decay (recent touches weighted more)
   - U-shaped (first + last touch weighted)
3. Run conversion path analysis:
   - Average touches to conversion by channel sequence
   - Which channel sequences have highest LTV
4. Recommend: current best-fit attribution model based on FKI data
5. Update CPA targets in Drive if attribution model changes significantly
6. Upload model analysis to Drive: `fki-intelligence/attribution-model-[date].md`
7. Post recommendation to #leo-auto

## DIAMOND GATE
- T1: Historical data only. Model is analytical ✅
- T2: File > 200 bytes ✅
- T3: Recommendation — Leo/Bennett approve model change ✅
