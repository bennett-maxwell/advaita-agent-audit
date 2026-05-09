# SKILL-181: Objection Library Builder
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Build and maintain FKI sales objection libraries. Every objection handled. Consistent responses across all touchpoints.

## TRIGGER
Monthly review (auto) OR 3+ new objection patterns detected in GHL call notes.

## EXECUTION STEPS
1. Pull GHL call notes and CRM entries from last 30d
2. Extract objection patterns (NLP matching):
   - Price objections ("too expensive", "can't afford")
   - Timing objections ("not right now", "next year")
   - Trust objections ("prove it works", "show me results")
   - Competitor objections ("I'm looking at [X]")
   - Spouse/partner objections
3. Run bennett-intelligence-layer-skill for objection response voice
4. Generate 3 response scripts per objection:
   - Acknowledge → reframe → evidence → ask
5. FDD qualifiers on all evidence/result responses
6. Upload to Drive: `fki-sales/[brand]-objection-library-v[X].md`
7. Post update count to #leo-auto

## DIAMOND GATE
- T1: FDD qualifiers on all evidence responses ✅
- T2: File > 200 bytes ✅
- T3: Document update — no auto-deploy to live scripts ✅
