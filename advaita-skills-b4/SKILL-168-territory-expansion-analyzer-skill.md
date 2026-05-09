# SKILL-168: Territory Expansion Analyzer
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Identify optimal markets for SRP franchise expansion. Data-driven territory prioritization.

## TRIGGER
Quarterly OR Bennett says "expansion analysis".

## EXECUTION STEPS
1. Load current territory map from Drive: `fki-franchise/territory-map.json`
2. Identify white-space markets (no existing franchisees within 50mi)
3. For each white-space market, score:
   - Population density (sports retail addressable market)
   - Household income (buying power for sports retail)
   - Competitor presence (lower = better)
   - Sports participation rate (proxy: gyms, rec centers per capita)
   - Commercial real estate availability and cost
4. Rank top 10 expansion markets
5. Generate one-page market brief per top 5:
   - Market size estimate
   - Competitive landscape
   - Site suggestions (general — not specific properties)
6. Upload to Drive: `fki-franchise/expansion-analysis-[date].md`
7. Post top 5 markets to #leo-auto

## DIAMOND GATE
- T1: Market data estimates only — no revenue projections ✅
- T2: File > 200 bytes ✅
- T3: Analysis only ✅
