---
skill: state-block-enforcement
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI enforces state registration blocks automatically — zero FDD compliance violations
---
# State Block Enforcement Skill v1

## Purpose
Hard enforcement of franchise state registration requirements. Brands cannot be marketed in states where they are not registered to offer franchises. This is a federal/state FTC compliance requirement.

## State Block Registry (current — verify with franchisor before any change)

**Indy Clover (IC)**
BLOCKED STATES (not registered): TX, NC, SC, FL, KY, ME, OR, UT
In any of these states: IC CANNOT appear in any marketing, recommendation, or communication to prospective buyers.

**Salad House (SH)**
BLOCKED STATES (not registered): CT, IL, MN, WA
In any of these states: SH CANNOT appear in any marketing, recommendation, or communication to prospective buyers.

**Spoiled Rotten Photography (SRP)**
No current state blocks. Available nationally. (Verify annually as registrations change.)

## Enforcement Points (check at each)

1. **Candidate intake**: When state identified → immediately filter blocked brands
2. **Brand recommendation**: Before generating shortlist → filter by state
3. **Content creation**: Any state-specific content → verify brand eligibility for that state
4. **Email sequences**: Any sequence with brand name → confirm recipient's state eligibility
5. **Ads**: Any geo-targeted ad → confirm brand is registered in geo target

## State Block Violation = CRITICAL
Any violation of state block rules is a compliance failure. Result:
- STOP output immediately
- Log to compliance record
- Post to #leo-auto as COMPLIANCE ALERT
- Do not attempt workaround

## Registry Update Protocol
State registrations change. AI cannot update this registry without Bennett approval. If franchisor notifies of new state registration → log to daily digest → Bennett approves update → AI updates registry.

## Autonomy Value
**Replaces:** Human manually checking state registration before every candidate conversation.
**Result:** Zero state block violations in any AI-generated content or recommendation. Compliance fully automated.
**Advaita gap closed:** State compliance enforcement — from 0% → 100% AI-autonomous.
