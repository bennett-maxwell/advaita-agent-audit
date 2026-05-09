# SKILL-104: Email Campaign Builder
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Build full email sequences for FKI offers. 5-email drip from opt-in to close. Brand voice matched. Loads to GHL automation.

## TRIGGER
Bennett says "build email sequence for [brand] [offer]".

## INPUTS
- Brand: IC | SH | SRP
- Offer name + price point
- Target ICP (new lead | warm lead | cold reactivation)
- Sequence length (default: 5 emails)

## EXECUTION STEPS
1. Load brand voice guide from Drive: `fki-brand-voice/[brand]-voice.md`
2. Run bennett-intelligence-layer-skill for brand-specific framing
3. Generate sequence:
   - Email 1: Welcome + quick win (Day 0)
   - Email 2: Core problem agitation (Day 1)
   - Email 3: Social proof + transformation story (Day 3)
   - Email 4: Objection crusher (Day 5)
   - Email 5: Urgency close (Day 7)
4. FDD qualifier on any $ result mention: "Results not typical. Individual results vary."
5. Format for GHL import (HTML + plain text variants)
6. Upload to Drive: `fki-email-sequences/[brand]-[offer]-sequence-[date].md`
7. Post receipt to #leo-auto with sequence summary + Drive link

## DIAMOND GATE
- T1: FDD qualifiers on all testimonials and $ figures ✅
- T2: File > 200 bytes ✅
- T3: Draft only — not loaded to GHL until Leo confirms ✅
