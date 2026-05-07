---
skill: investment-range-filter
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI enforces investment range filters — no broker ever presents a brand a candidate can't afford
---
# Investment Range Filter Skill v1

## Purpose
Hard filter that prevents any brand from being presented to a candidate whose liquid capital falls below that brand's FDD Item 7 minimum. Saves discovery time and prevents disappointment.

## Filter Logic

**Input**: Candidate liquid capital (confirmed) + net worth (approximate)
**Data source**: Each brand's FDD Item 7 total estimated initial investment range (results may vary; see FDD for current figures)

## Brand Eligibility Gates

Filter is HARD — brand is excluded from recommendation if candidate liquid < brand minimum (per FDD Item 7; results may vary).

## Capital Cushion Rule
AI recommends candidate retain minimum 6 months of living expenses + brand investment minimum. Candidates investing their last dollar into a franchise are high-risk.

If liquid capital minus investment minimum leaves < 3 months living expenses → FLAG for funding conversation before presenting brand.

## Communication Language
When brand is filtered: "Based on the investment range in their FDD, we'd want to confirm your capital position before exploring this brand further. There are other strong options within your current range."

NEVER say "you can't afford that" — frame as timing and fit.

## Autonomy Value
**Replaces:** Broker awkwardly discovering capital shortfall mid-discovery call.
**Result:** Every recommendation is within reach. Zero wasted discovery conversations on unaffordable brands.
**Advaita gap closed:** Capital eligibility filtering — from 0% → 100% AI-autonomous.
