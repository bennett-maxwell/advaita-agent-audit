# SKILL-183: Retargeting Ad Copy Generator
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Generate retargeting ad copy for warm Meta/Google audiences. Higher-intent messaging for people who already know the brand.

## TRIGGER
Bennett says "retargeting copy [brand] [offer]" OR weekly creative refresh.

## EXECUTION STEPS
1. Run bennett-intelligence-layer-skill
2. Identify retargeting audience temperature:
   - Warm (visited site, engaged social): soft sell, value add
   - Hot (abandoned checkout, booked not enrolled): urgency close
   - Reactivation (past client 90d+ inactive): nostalgia + new angle
3. Generate 5 ad variations per temperature:
   - Headline (25 chars)
   - Primary text (125 chars)
   - Description (30 chars)
   - CTA button text
4. FDD qualifiers on any result claims
5. Upload to Drive: `fki-content/ads/[brand]-retargeting-[date].md`
6. Post to #leo-auto with temperature levels + Drive link

## DIAMOND GATE
- T1: FDD qualifiers on results ✅
- T2: File > 200 bytes ✅
- T3: Copy draft — no auto-launch ✅
