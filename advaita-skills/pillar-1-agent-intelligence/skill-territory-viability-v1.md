---
skill: territory-viability-analysis
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI analyzes territory fit before candidate commits — replaces manual gut-feel geo checks
---
# Territory Viability Analysis Skill v1

## Purpose
Before a candidate commits to a territory, AI runs a viability check across 5 dimensions and produces a GO / CONDITIONAL / NO-GO recommendation.

## Analysis Dimensions

**1. Population and Demographics**
- Target population density for brand type (service vs food vs retail)
- Median household income alignment with brand's customer profile
- Age demographic fit

**2. Competition Density**
- Existing franchise locations in territory (same brand — check MapKi)
- Competitive brand saturation (direct competitors)
- White space opportunity scoring

**3. Business Environment**
- Local business growth trend (3-year)
- Employment rate (proxy for consumer spending)
- Real estate availability and cost trend for brand's format

**4. Brand State Eligibility**
- Confirm territory state is NOT on brand's blocked list
- IC blocked: TX, NC, SC, FL, KY, ME, OR, UT
- SH blocked: CT, IL, MN, WA
- SRP: no state blocks

**5. Candidate Personal Fit**
- Candidate already lives in / near territory?
- Community connection (IC specifically requires community engagement)
- Prior market knowledge

## Output Format
GO: Territory shows positive signals across all 5 dimensions. Recommend proceeding.
CONDITIONAL GO: 1–2 dimensions have yellow flags — specific concerns listed.
NO-GO: Critical blocker identified (state block, saturation, demographic mismatch).

## Autonomy Value
**Replaces:** Broker making geographic calls from memory.
**Result:** Every territory decision is data-backed. Reduces post-sale regret.
**Advaita gap closed:** Territory analysis — from 0% → 80% AI-autonomous.
