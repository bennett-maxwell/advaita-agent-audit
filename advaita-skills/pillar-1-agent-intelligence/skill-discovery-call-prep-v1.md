---
skill: discovery-call-prep
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI briefs broker before every discovery call — broker shows up prepared, not winging it
---
# Discovery Call Prep Skill v1

## Purpose
Before every discovery call, AI generates a 1-page brief for the broker: candidate summary, top 3 brands to discuss, likely objections, and recommended call flow.

## Trigger
GHL stage change to "Discovery Scheduled" OR calendar event with candidate name.

## Brief Structure

**Section 1 — Candidate Snapshot (auto-pulled from GHL)**
- Name, location, liquid capital range, stated timeline
- Source / how they found FKI
- Prior touchpoints (emails opened, pages visited, form responses)
- FranchiseScore + tier

**Section 2 — Recommended Brand Discussion Order**
Top 3 brands from recommendation engine output, with 1-line "why this fits them" for each.

**Section 3 — Likely Objections + AI-Suggested Responses**
Based on candidate profile and common objection patterns:
- "I'm not sure I have enough capital" → funding paths available (per FDD; results may vary)
- "My spouse isn't fully on board" → alignment conversation framework
- "I want to think about it more" → urgency reframe (territory availability)
- "I've heard franchises fail" → validation call approach, Item 19 data (see FDD; results may vary)

**Section 4 — Recommended Call Flow**
1. Rapport (2 min) — reference their specific background
2. Motivation deep-dive (8 min) — what's driving the decision NOW
3. Lifestyle design (5 min) — what does success look like in 3 years
4. Brand intro (10 min) — present top 2 brands, reaction check
5. Next step lock (5 min) — FDD request or brand discovery call

## Delivery
Brief posted to #leo-auto AND saved to candidate's GHL note field before call time.

## Autonomy Value
**Replaces:** Broker manually reviewing notes 5 min before call.
**Result:** Every call starts with full context. Close rate increases.
**Advaita gap closed:** Call prep — from 0% → 100% AI-autonomous.
