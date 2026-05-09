# SKILL-133: CPA Target Monitor
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor cost-per-acquisition vs target across all FKI campaigns and channels. Auto-flag when CPA exceeds threshold.

## TRIGGER
Daily 7 AM MDT (auto).

## EXECUTION STEPS
1. Pull Meta Ads API: spend + conversions per campaign (last 7d)
2. Pull GHL: new enrollments with source tag (last 7d)
3. Pull QB: revenue per enrollment (last 7d)
4. Calculate CPA by campaign: Spend / Conversions
5. Load CPA targets from Drive: `fki-finance/cpa-targets.md`
   - IC coaching: $[target from Drive]
   - SH coaching: $[target from Drive]
   - SRP franchise: $[target from Drive]
6. Flag: any campaign CPA > 150% of target → work order to Leo to pause/adjust
7. Upload daily CPA table to Drive: `fki-reports/cpa-daily-[date].md`
8. Post flags to #leo-auto immediately

## DIAMOND GATE
- T1: Actual API data only ✅
- T2: File > 200 bytes ✅
- T3: Alert only — Leo executes campaign changes ✅
