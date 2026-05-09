# SKILL-115: SH Pricing Defense Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
When prospects ask about price or push back, generate FKI-aligned value-anchoring responses. Protects SH price integrity without Bennett on the call.

## TRIGGER
GHL contact note contains "price objection" OR Bennett says "SH price defense script".

## EXECUTION STEPS
1. Run bennett-intelligence-layer-skill for current SH positioning
2. Load SH objection library from Drive: `fki-sales/sh-objections.md`
3. Generate 3 price defense scripts:
   - Anchor to transformation value (ROI frame)
   - Competitor comparison (without naming competitors)
   - Payment plan option presentation
4. FDD qualifier: "Results not typical. Individual results will vary based on effort and market conditions."
5. Upload scripts to Drive: `fki-sales/sh-price-defense-[date].md`
6. Post to #leo-auto

## DIAMOND GATE
- T1: No income guarantees. FDD on all examples ✅
- T2: File > 200 bytes ✅
- T3: Draft scripts — no action ✅
