# SKILL-119: SRP Item 7 Investment Builder
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Build FDD Item 7 (estimated initial investment) tables for SRP franchise candidates. Pulls current cost data, formats per FTC requirements.

## TRIGGER
Bennett says "build SRP Item 7" OR new FDD revision cycle.

## EXECUTION STEPS
1. Load current SRP cost inputs from Drive: `fki-franchise/item7-inputs.md`:
   - Initial franchise fee
   - Equipment and inventory ranges
   - Leasehold improvements (low/high)
   - Training expenses
   - Working capital (3-month estimate)
   - Misc/professional fees
2. Format as Item 7 table (FTC-compliant column headers)
3. Add Item 7 compliance language:
   - "These figures are estimates only. Actual costs may vary."
   - "You should review these figures with a professional advisor."
4. Upload draft to Drive: `fki-franchise/fdd-drafts/item7-[date].md`
5. Flag: "LEGAL REVIEW REQUIRED before inclusion in FDD"
6. Post receipt to #leo-auto — DO NOT distribute to candidates without legal review

## DIAMOND GATE
- T1: Estimates only — no guarantees. Legal review flag ✅
- T2: File > 200 bytes ✅
- T3: Draft only — requires Bennett legal gate before distribution ✅
