# SKILL-184: PR Story Generator
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Generate press release drafts and media pitch angles for FKI brand milestones, launches, and newsworthy events.

## TRIGGER
Bennett says "PR for [event/launch]" OR milestone hit (new franchisee opened, coaching cohort launch, partnership).

## EXECUTION STEPS
1. Run bennett-intelligence-layer-skill for current brand narrative
2. Identify story angle:
   - Business milestone (funding, expansion, new product)
   - Human interest (transformation story — with consent)
   - Industry commentary (Bennett as expert source)
   - Community impact (local SRP franchise, IC clinic)
3. Draft press release:
   - Headline (AP style)
   - Dateline + lead paragraph (who/what/when/where/why)
   - 2-3 body paragraphs
   - Quote from "Bennett Maxwell, Founder, FKI"
   - Boilerplate (company description)
   - Contact info
4. FDD qualifier if any financial figures mentioned
5. Upload to Drive: `fki-marketing/pr/[brand]-pr-[date]-[slug].md`
6. Post to #leo-auto — Leo distributes to media list

## DIAMOND GATE
- T1: FDD qualifier on any $ figures ✅
- T2: File > 200 bytes ✅
- T3: Draft — Leo distributes ✅
