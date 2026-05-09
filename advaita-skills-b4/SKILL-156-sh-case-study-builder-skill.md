# SKILL-156: SH Case Study Builder
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Build FDD-compliant case studies from SH client success stories. Ready for use in marketing with proper disclaimers.

## TRIGGER
Client cleared testimonial (SKILL-122) AND revenue milestone hit.

## EXECUTION STEPS
1. Pull client testimonial from Drive: `fki-marketing/testimonials/sh-testimonials.md`
2. Pull client milestones from GHL notes
3. Run bennett-intelligence-layer-skill for narrative framing
4. Draft case study:
   - Client background (anonymized if requested)
   - Challenge before SH
   - Coaching process (3-4 bullets)
   - Results achieved (specific numbers if cleared)
   - Key lessons / transferable insights
5. MANDATORY footer: "Results not typical. Individual results will vary based on effort, market conditions, consistency of implementation, and prior experience. This case study represents one client's experience."
6. If specific $ figures: add "Financial results reflect this individual's experience and are not a prediction of your results."
7. Upload to Drive: `fki-marketing/case-studies/sh-[client-id]-[date].md`
8. Tag "CLEARED" in Drive — cleared for marketing use
9. Post to #leo-auto

## DIAMOND GATE
- T1: Full FDD disclaimer mandatory — built into template ✅
- T2: File > 200 bytes ✅
- T3: Document only ✅
