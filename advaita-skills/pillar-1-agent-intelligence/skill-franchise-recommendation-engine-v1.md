---
skill: franchise-recommendation-engine
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI generates brand shortlist — replaces broker memory and gut-feel brand matching
---
# Franchise Recommendation Engine Skill v1

## Purpose
Given a qualified candidate profile, AI generates a ranked brand shortlist of 3–5 franchises with match rationale. Replaces broker manually recalling brand options.

## Input: Candidate Profile
Required fields: liquid capital range, net worth (approximate), timeline, geographic market, lifestyle goal (semi-absentee / owner-operator / investor), industry preference (if any), prior experience.

## Matching Logic (sequential filters)

**Filter 1 — Capital Eligibility**
Remove all brands requiring liquid capital > candidate maximum (per FDD Item 7 disclosures; results may vary, see FDD for details).

**Filter 2 — State Eligibility**
Remove blocked brands per candidate's target states (IC: TX/NC/SC/FL/KY/ME/OR/UT; SH: CT/IL/MN/WA).

**Filter 3 — Lifestyle Fit**
Semi-absentee goal → prioritize IC, SRP (manager-run models)
Owner-operator goal → prioritize SH (hands-on, high AUV)
Investor/passive goal → IC semi-absentee pathway

**Filter 4 — Investment Appetite**
Match candidate's stated investment comfort zone to brand Item 7 ranges (see FDD; results may vary).

**Filter 5 — Market Availability**
Check territory availability for candidate's target geography before presenting brand.

## Output Format
For each recommended brand:
- Brand name + concept summary
- Why it fits this specific candidate (2–3 sentences)
- Investment range reference (see FDD for exact figures; results may vary)
- Key due diligence questions to ask

## Autonomy Value
**Replaces:** Broker spending 20–45 min thinking through brand options per candidate.
**Result:** AI delivers shortlist in <10 seconds. Broker focuses on relationship, not recall.
**Advaita gap closed:** Brand matching — from 0% → 90% AI-autonomous (broker validates fit).
