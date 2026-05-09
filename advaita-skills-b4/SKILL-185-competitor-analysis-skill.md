# SKILL-185: Competitor Analysis Automation
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Monthly competitive landscape analysis for each FKI brand. Surface threats, opportunities, and positioning gaps.

## TRIGGER
Monthly 20th (auto) OR Bennett says "competitor analysis [brand]".

## EXECUTION STEPS
1. Run Exa search for each brand's top 5 competitors (updated monthly)
2. For each competitor: pull
   - Pricing (public)
   - Offer structure
   - Recent ad campaigns (Meta Ad Library)
   - Review sentiment (G2, Yelp, Google)
   - Social following growth
3. Build competitive matrix:
   - FKI brand vs each competitor on: Price / Positioning / Proof / Platform / Reach
4. Identify:
   - Where FKI is clearly stronger (reinforce in marketing)
   - Where competitors are gaining ground (counter-strategy)
   - White-space positioning opportunities
5. Upload to Drive: `fki-marketing/competitor-analysis/[brand]-[date].md`
6. Post key findings (2-3 bullets) to #leo-auto

## DIAMOND GATE
- T1: Public data only. No false claims about competitors ✅
- T2: File > 200 bytes ✅
- T3: Research document ✅
