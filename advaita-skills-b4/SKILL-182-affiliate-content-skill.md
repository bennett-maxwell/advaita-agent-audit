# SKILL-182: Affiliate Content Generator
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Generate promotional content for FKI affiliate/ambassador partners. FDD-compliant. Brand voice consistent.

## TRIGGER
New affiliate activated (ThriveCart event) OR monthly affiliate content refresh.

## EXECUTION STEPS
1. Pull affiliate profile from ThriveCart: name, niche, audience size
2. Run bennett-intelligence-layer-skill for brand framing
3. Generate affiliate content package:
   - 3 email swipe copy options (different angles)
   - 5 social media caption options
   - 1 video testimonial outline (if applicable)
   - Tracking link + UTM instructions
4. MANDATORY in all affiliate materials:
   - "#ad" or "Sponsored" disclosure for paid partnerships
   - FDD qualifier on any income/result claims
   - "Results not typical. Individual results will vary."
5. Upload to Drive: `fki-marketing/affiliates/[affiliate-id]-content-[date].md`
6. Send to affiliate via email with Drive link
7. Post to #leo-auto: affiliate name + content package sent

## DIAMOND GATE
- T1: FTC ad disclosure + FDD qualifiers mandatory ✅
- T2: File > 200 bytes ✅
- T3: Content package send REVERSIBLE ✅
