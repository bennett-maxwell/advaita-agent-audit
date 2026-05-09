# SKILL-118: SRP Territory Mapping Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-map available SRP franchise territories based on candidate location, existing franchise proximity, and market density data.

## TRIGGER
SRP franchise candidate advances to territory review stage.

## EXECUTION STEPS
1. Pull candidate address from GHL
2. Load existing SRP territory map from Drive: `fki-franchise/territory-map.json`
3. Check 50-mile exclusivity radius for existing franchisees
4. Run market density analysis:
   - Sports retail market size (from Drive data)
   - Population density
   - Competitor count in territory
5. Generate territory recommendation: Primary + 2 alternatives
6. Create territory map visual (Markdown table with city/zip data)
7. Upload to Drive: `fki-franchise/territory-proposals/[candidate-id]-territory.md`
8. Post to #leo-auto with Drive link

## DIAMOND GATE
- T1: No revenue projections for territory ✅
- T2: File > 200 bytes ✅
- T3: Proposal only — no territory locked until legal sign-off ✅
