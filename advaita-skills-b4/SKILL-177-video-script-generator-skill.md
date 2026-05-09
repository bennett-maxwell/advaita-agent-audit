# SKILL-177: Video Script Generator
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Generate full video scripts for FKI brand content: YouTube, course content, ads, testimonials, podcast clips.

## TRIGGER
Bennett says "script for [video type] [topic] [brand]".

## EXECUTION STEPS
1. Run bennett-intelligence-layer-skill
2. Load brand voice + target audience for brand
3. Determine video type and adjust format:
   - YouTube (5-15 min): hook + story + value + CTA structure
   - Course module (3-8 min): teach + demo + recap
   - Ad (30-90 sec): hook + problem + solution + proof + CTA
   - Testimonial guide (2-3 min): situation → struggle → solution → result → recommend
   - Podcast clip (60-90 sec): insight + story + takeaway
4. Write full script with:
   - [SCREEN] / [CUT] / [B-ROLL] direction notes
   - Emphasis marks for key phrases
   - Pause indicators
5. FDD qualifiers on any result/income mentions
6. Upload to Drive: `fki-content/scripts/[brand]-[date]-[type].md`
7. Post to #leo-auto

## DIAMOND GATE
- T1: FDD qualifiers in script. bennett-intelligence-layer mandatory ✅
- T2: File > 200 bytes ✅
- T3: Script document only ✅
