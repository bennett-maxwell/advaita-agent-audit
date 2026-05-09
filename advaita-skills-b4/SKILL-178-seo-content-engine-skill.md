# SKILL-178: SEO Content Engine
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Generate SEO-optimized blog content targeting FKI brand keywords. Organic search acquisition at zero ad cost.

## TRIGGER
Monthly SEO content calendar OR Bennett says "SEO post [brand] [keyword]".

## EXECUTION STEPS
1. Run Exa search: target keyword volume and competition (brand-specific)
2. Run bennett-intelligence-layer-skill for brand voice
3. Identify keyword cluster:
   - Primary keyword (high intent)
   - 3-5 semantic LSI keywords
   - Featured snippet opportunity (question-based)
4. Generate SEO-optimized post:
   - H1: primary keyword + brand hook
   - H2s: semantic clusters + FAQ
   - 1,200-2,000 words
   - Internal link suggestions
   - Meta description (155 chars)
5. FDD qualifiers on all result claims
6. Upload to Drive: `fki-content/seo/[brand]-[keyword-slug]-[date].md`
7. Post to #leo-auto with primary keyword + estimated monthly searches

## DIAMOND GATE
- T1: FDD qualifiers on results. No false search volume claims ✅
- T2: File > 200 bytes ✅
- T3: Draft — no auto-publish ✅
