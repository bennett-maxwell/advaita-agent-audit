# SKILL-135: Budget Pacing Monitor
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor monthly ad spend pacing across all FKI brands. Ensure spend doesn't overshoot budget before month end.

## TRIGGER
Daily 8 AM MDT (auto).

## EXECUTION STEPS
1. Pull Meta Ads API: month-to-date spend by brand ad account
2. Pull Google Ads API: month-to-date spend
3. Load monthly budgets from Drive: `fki-finance/monthly-ad-budgets.md`
4. Calculate pacing:
   - Days elapsed / Days in month = Expected % spent
   - Actual % spent vs expected %
5. Flag conditions:
   - Overpacing > 15%: alert Leo to reduce daily budgets
   - Underpacing > 20%: opportunity to increase (post suggestion)
6. Upload pacing report to Drive: `fki-reports/budget-pacing-[date].md`
7. Post daily pacing summary to #leo-auto

## DIAMOND GATE
- T1: Actual spend data only ✅
- T2: File > 200 bytes ✅
- T3: Alert + suggestion only — Leo executes budget changes ✅
