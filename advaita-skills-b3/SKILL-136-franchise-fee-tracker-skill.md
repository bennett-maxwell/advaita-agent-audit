# SKILL-136: Franchise Fee Tracker
**Version:** 1.0 | **Pillar:** Financial Modeling | **Reversibility:** REVERSIBLE

## PURPOSE
Track royalty and ad fund collection from SRP franchisees. Flag past-due payments. Generate receivables aging report.

## TRIGGER
Monthly 5th (auto) OR Bennett says "franchise fees".

## EXECUTION STEPS
1. Pull SRP franchisee list from Drive: `fki-franchise/franchisee-roster.md`
2. Pull QuickBooks: franchise fee payments received current month
3. Compare expected vs received:
   - Royalty: [% from FDD] × franchisee gross sales
   - Ad fund contribution: [% from FDD] × franchisee gross sales
4. Flag: past-due > 30d → work order to Leo for collection outreach
5. Flag: past-due > 60d → escalate to Bennett (legal gate threshold)
6. Generate AR aging table (current / 30d / 60d / 90d+)
7. Upload to Drive: `fki-franchise/fee-collection-[month]-[year].md`
8. Post monthly summary to #leo-auto

## DIAMOND GATE
- T1: Actual collection data — no projections ✅
- T2: File > 200 bytes ✅
- T3: Report only — collection actions via Leo ✅
