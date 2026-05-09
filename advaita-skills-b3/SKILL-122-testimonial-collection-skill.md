# SKILL-122: Testimonial Collection Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-collect and process client testimonials across all FKI brands. Screen for FDD compliance. Route to marketing team.

## TRIGGER
GHL event: client completes week 4, week 8, or graduation milestone.

## EXECUTION STEPS
1. Trigger testimonial request email (from Drive template by brand)
2. Collect responses via Typeform or GHL survey
3. Screen response:
   - Contains specific $ figures → flag for legal review before use
   - Contains timeframe claims → add "results not typical" disclaimer
   - No specific claims → cleared for immediate use
4. Log to Drive: `fki-marketing/testimonials/[brand]-testimonials.md`
5. Add "CLEARED" or "LEGAL REVIEW" tag to each testimonial
6. Post new cleared testimonials to #leo-auto weekly

## COMPLIANCE
All testimonials used in marketing must include: "Results not typical. Individual results may vary based on effort, experience, and market conditions."

## DIAMOND GATE
- T1: FDD compliance screening built-in ✅
- T2: File > 200 bytes ✅
- T3: Collection REVERSIBLE. No auto-publish ✅
