---
skill: lead-qualification
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: Replaces manual broker lead review — AI scores every inbound lead in <60s
---
# Lead Qualification Skill v1

## Purpose
AI qualifies every inbound GHL lead without human review. Outputs: QUALIFIED / NURTURE / DISQUALIFY with reasoning.

## Input
GHL contact record: name, email, phone, source, form answers, investment range indicated.

## Qualification Decision Tree
**Step 1 — Liquid Capital Check**
- Stated liquid capital ≥ minimum threshold for any FKI brand → PROCEED
- Below threshold → tag NURTURE, trigger 90-day re-engagement sequence
- No capital stated → trigger clarification sequence (auto-email), hold 48h

**Step 2 — Timeline Check**
- Timeline stated ≤ 24 months → PROCEED
- Timeline > 24 months → NURTURE (long-cycle sequence)
- "Just researching" / no timeline → NURTURE

**Step 3 — Motivation Check**
- W2 replacement / income diversification / semi-absentee → HIGH FIT
- Pure investment / passive only → MEDIUM FIT (brand match required)
- Already has business → assess capacity, flag for broker review

**Step 4 — Geographic Check**
- Not in any brand's blocked state → PROCEED
- In IC-blocked state (TX, NC, SC, FL, KY, ME, OR, UT) → remove IC from match set
- In SH-blocked state (CT, IL, MN, WA) → remove SH from match set

## Output Tags (GHL)
- `ai-qualified` — passed all 4 steps
- `ai-nurture-capital` — failed capital step
- `ai-nurture-timeline` — failed timeline step
- `ai-disqualify` — not a franchise buyer profile
- `ai-hold-info-needed` — awaiting clarification

## Autonomy Value
**Replaces:** Broker spending 15–30 min per lead reviewing manually.
**Result:** Brokers only touch QUALIFIED leads. AI handles 100% of initial triage.
**Advaita gap closed:** Lead qualification — from 0% → 100% AI-autonomous.
