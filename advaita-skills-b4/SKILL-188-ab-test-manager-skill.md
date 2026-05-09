# SKILL-188: A/B Test Manager
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Design, track, and analyze A/B tests across FKI marketing and sales touchpoints. Systematize what works.

## TRIGGER
Bennett says "A/B test [element] [brand]" OR weekly performance review flags underperformer worth testing.

## EXECUTION STEPS
1. Define test:
   - Element: headline / CTA / offer frame / email subject / landing page
   - Hypothesis: "Changing X to Y will improve metric Z by W%"
   - Control: current version (A)
   - Variant: new version (B)
   - Sample size: minimum for statistical significance (95% confidence)
   - Duration: typically 7-14 days
2. Set up in Meta/GHL as appropriate
3. Log test to Drive: `fki-intelligence/ab-tests/[test-id]-[date].md`
4. Daily: check if significance threshold reached
5. On significance: declare winner, log result, update templates
6. Post test results to #leo-auto when concluded

## DIAMOND GATE
- T1: Statistical methodology disclosed. No cherry-picking ✅
- T2: File > 200 bytes ✅
- T3: Test setup REVERSIBLE ✅
