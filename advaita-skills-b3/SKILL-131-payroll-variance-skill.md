# SKILL-131: Payroll Variance Monitor
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor payroll actuals vs budget. Flag overruns. Ensure FKI stays within compensation model targets.

## TRIGGER
Weekly Friday 5 PM MDT (auto) OR after each payroll run.

## EXECUTION STEPS
1. Pull payroll data from QuickBooks (last pay period)
2. Load payroll budget from Drive: `fki-finance/payroll-budget.md`
3. Compare actual vs budget by:
   - Department (ops, marketing, coaching, admin)
   - Individual vs total
4. Flag: any line item > 10% over budget
5. Calculate: payroll as % of gross revenue (target < 30%)
6. If payroll/revenue > 35%: RED alert to #leo-auto
7. Upload variance report to Drive: `fki-finance/payroll-variance-[date].md`
8. Post summary to #leo-auto

## DIAMOND GATE
- T1: Actual QB figures only ✅
- T2: File > 200 bytes ✅
- T3: Read-only reporting ✅
