# SKILL-176: Bennett Voice Content Engine
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Generate long-form content (blogs, LinkedIn articles, podcast outlines) in Bennett's authentic voice across all FKI brands.

## TRIGGER
Bennett says "write [content type] about [topic]" OR weekly content calendar requires long-form.

## EXECUTION STEPS
1. ALWAYS run bennett-intelligence-layer-skill first — mandatory before any content
2. Load brand voice guide for relevant brand
3. Identify content type:
   - Blog post: 800-1200 words, SEO-structured
   - LinkedIn article: 500-800 words, thought leadership
   - Podcast outline: 30-45 min with timestamps
   - Email newsletter: 400-600 words, personal tone
4. Generate content in Bennett's voice:
   - First person, conversational, direct
   - Story-based, personal anecdotes
   - Clear POV, opinionated
   - CTA appropriate for brand/funnel stage
5. FDD qualifiers on any income/result mentions
6. Upload to Drive: `fki-content/long-form/[brand]-[date]-[slug].md`
7. Post to #leo-auto with content type + word count + Drive link

## DIAMOND GATE
- T1: FDD qualifiers on results. bennett-intelligence-layer mandatory ✅
- T2: File > 200 bytes ✅
- T3: Content draft — no auto-publish ✅
