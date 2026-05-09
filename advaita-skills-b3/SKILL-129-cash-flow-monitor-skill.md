# SKILL-129: Cash Flow Monitor Automation
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Real-time cash flow monitoring across FKI entities. 30/60/90-day projection from QB actuals + pipeline.

## TRIGGER
Daily 6:30 AM MDT (auto) OR Bennett says "cash flow".

## EXECUTION STEPS
1. Pull QuickBooks:
   - Current cash balance (checking + savings)
   - Accounts receivable (30/60/90d aging)
   - Accounts payable due next 90d
   - Recurring revenue (subscription MRR)
2. Pull GHL:
   - Open pipeline value (hot leads × avg close rate)
3. Build 90-day projection:
   - Cash in: AR + pipeline (probability-weighted)
   - Cash out: AP + projected payroll + ad spend
   - Net position by week
4. Flag: week where projected balance < $50K → RED alert to #leo-auto
5. Upload projection to Drive: `fki-finance/cash-flow-[date].md`
6. Post daily summary (balance, 30d projection) to #leo-auto

## DIAMOND GATE
- T1: Projections labeled "estimates based on historical data" ✅
- T2: File > 200 bytes ✅
- T3: Read-only ✅
