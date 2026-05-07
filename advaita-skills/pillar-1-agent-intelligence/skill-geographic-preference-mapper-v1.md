---
skill: geographic-preference-mapper
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI maps geographic preferences to territory availability — prevents presenting unavailable territories
---
# Geographic Preference Mapper Skill v1

## Purpose
Systematically capture, store, and cross-check candidate geographic preferences against territory availability for each brand. Never present an unavailable territory.

## Geographic Data Capture (from intake form + discovery call)

**Primary Market**: City/MSA where candidate wants their first unit
**Secondary Market**: Acceptable alternatives if primary is taken
**Hard No's**: Markets candidate explicitly rejects (don't waste time here)
**Geographic Flexibility Score**: 1 (very locked) to 5 (very flexible)

## Territory Availability Check (per brand)

For each brand in candidate's shortlist:
1. Check MapKi for territory status in candidate's primary market
2. Check brand's territory map (from FDD Item 12 and franchisor inquiry)
3. Flag: AVAILABLE / PENDING / TAKEN / UNKNOWN (follow up with franchisor)

## State Block Cross-Check
- IC: TX, NC, SC, FL, KY, ME, OR, UT → remove IC if primary or secondary market is in blocked state
- SH: CT, IL, MN, WA → remove SH if market is in blocked state
- SRP: No state blocks

## Output: Territory Status Report (per candidate)
For each brand × market combination:
- Territory status + confidence level
- Competing candidate presence (if known)
- Urgency signal: "1 territory remaining in [market]" → activate urgency messaging

## Autonomy Value
**Replaces:** Broker manually checking territory availability for each candidate.
**Result:** Zero time spent discussing unavailable territories. Every conversation is about real options.
**Advaita gap closed:** Territory availability intelligence — from 0% → 100% AI-autonomous.
