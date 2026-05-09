# SKILL-107: Webinar Funnel Automation
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Build complete webinar registration and follow-up funnel. Registration page, reminder sequence, replay sequence, offer close sequence.

## TRIGGER
Bennett says "webinar funnel [brand] [topic] [date]".

## EXECUTION STEPS
1. Load brand funnel template from Drive: `fki-funnels/[brand]-webinar-template.md`
2. Generate:
   - Registration page copy (headline, bullets, CTA)
   - 3-email reminder sequence (24h, 1h, live)
   - 5-email post-webinar sequence (replay, FAQ, close, urgency, final call)
   - SMS reminder (24h + 15min before)
3. Run bennett-intelligence-layer-skill for brand voice alignment
4. Add FDD qualifiers to all result claims
5. Export all assets to Drive: `fki-funnels/[brand]-[date]-webinar-assets/`
6. Create GHL workflow skeleton (not activated)
7. Post asset index to #leo-auto

## DIAMOND GATE
- T1: FDD on all testimonials and income examples ✅
- T2: File > 200 bytes ✅
- T3: Assets draft only — GHL workflow not activated ✅
