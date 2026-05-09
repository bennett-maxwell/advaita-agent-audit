# SKILL-198: Monthly Close Orchestrator
**Version:** 1.0 | **Pillar:** Autonomy Glue | **Reversibility:** REVERSIBLE

## PURPOSE
Month-end automation sequence. Close the books, review all brands, update forecasts, plan next month. Zero manual oversight required.

## TRIGGER
Last calendar day of month, 8:00 PM MDT (auto).

## EXECUTION SEQUENCE
1. SKILL-137: Final Monthly P&L
2. SKILL-162: Cross-Brand Monthly Report
3. SKILL-134: LTV Analysis
4. SKILL-132: Revenue Attribution
5. SKILL-136: Franchise Fee Collection
6. SKILL-186: Pattern Learning Engine
7. SKILL-189: Attribution Model Tuner
8. SKILL-149: Team Performance Review
9. SKILL-194: Forecast Builder (next quarter if month = March/June/Sep/Dec)
10. SKILL-195: Innovation Pipeline Review

## OUTPUT
- Month-end summary post to #leo-auto by 9:00 PM
  "📊 MONTH END — [Month Year]
  Revenue: $X (↑/↓ X% MoM)
  Top performer: [brand]
  Key pattern: [top learning]
  Next month focus: [top priority]"
- All individual skill receipts logged

## DIAMOND GATE
- T1: Aggregate of compliant skills ✅
- T2: File > 200 bytes ✅
- T3: All constituent skills REVERSIBLE ✅
