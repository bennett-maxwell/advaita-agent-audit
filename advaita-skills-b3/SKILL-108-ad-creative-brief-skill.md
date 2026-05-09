# SKILL-108: Ad Creative Brief Generator
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Generate production-ready ad creative briefs for FKI video and static ads. Brief includes hook, body, CTA, B-roll notes, talent direction.

## TRIGGER
Bennett says "creative brief [brand] [offer] [format]".

## EXECUTION STEPS
1. Run bennett-intelligence-layer-skill: pull winning hook patterns from last 30d
2. Generate 3 concept variants:
   - Concept A: Pain-agitate-solve structure
   - Concept B: Social proof lead
   - Concept C: Curiosity/pattern interrupt hook
3. For each concept:
   - Hook (0-3 sec): exact script
   - Body (3-20 sec): key message + proof point
   - CTA (final 3 sec): offer + urgency
   - Visual notes: B-roll, text overlays, color palette
   - Talent direction: tone, energy, wardrobe
4. Upload brief to Drive: `fki-creatives/briefs/[brand]-[date]-creative-brief.md`
5. Post to #leo-auto with Drive link

## DIAMOND GATE
- T1: No income figures in brief without FDD qualifier ✅
- T2: File > 200 bytes ✅
- T3: Brief document — no spend committed ✅
