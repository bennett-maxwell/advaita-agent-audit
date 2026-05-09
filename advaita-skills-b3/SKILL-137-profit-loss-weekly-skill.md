# SKILL-137: Weekly P&L Automation
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Generate weekly P&L summary from QuickBooks for Bennett. Delta from prior week highlighted. No accountant required.

## TRIGGER
Monday 7 AM MDT (auto) OR Bennett says "P&L".

## EXECUTION STEPS
1. Pull QuickBooks:
   - Gross revenue (week)
   - COGS (week)
   - Operating expenses (week)
   - Net operating income
   - Cash balance
2. Compare to prior week (QB prior period)
3. Calculate:
   - Gross margin % (and change)
   - Operating margin % (and change)
   - Revenue growth % WoW
4. Format 1-page P&L with delta arrows (↑↓)
5. Flag: any expense category > 20% WoW increase
6. Upload to Drive: `fki-finance/pl-weekly-[date].md`
7. Post 4-line summary to #leo-auto (Revenue / GM% / OpInc / Cash)

## DIAMOND GATE
- T1: QB actuals only ✅
- T2: File > 200 bytes ✅
- T3: Read-only ✅
