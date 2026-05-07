---
skill: ghl-lead-intake
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI reads every new GHL lead automatically — replaces manual CRM monitoring
---
# GHL Lead Intake Skill v1

## Purpose
Every time a new lead enters GHL, AI automatically reads the contact record, runs qualification checks, and routes appropriately — without broker checking CRM.

## Trigger
GHL webhook on new contact creation OR GHL tag change to `new-lead`.

## Auto-Actions on New Lead (all REVERSIBLE)
1. Pull full contact record: name, email, phone, source, form responses, custom fields
2. Run skill-lead-qualification-v1 → assign qualification tag
3. Run skill-candidate-scoring-v1 → assign FranchiseScore
4. Run skill-geographic-preference-mapper-v1 → map state eligibility
5. Run skill-franchise-recommendation-engine-v1 → generate initial brand shortlist
6. Apply result tags to GHL contact
7. Route: QUALIFIED → broker notification within 15 min; NURTURE → sequence enrollment; DISQUALIFY → archive

## GHL Field Mapping (read)
- `contact.firstName`, `contact.lastName` → candidate name
- `contact.email`, `contact.phone` → contact details
- `contact.source` → lead source attribution
- `custom_fields.liquid_capital` → capital qualification
- `custom_fields.timeline` → timeline qualification
- `custom_fields.target_state` → geographic routing
- `custom_fields.lifestyle_goal` → semi-absentee vs. owner-operator

## Error Handling
If GHL record is missing required fields → trigger clarification auto-email + tag `ai-info-needed`
If GHL API returns error → log to ERRORS.md + retry once → if still failing → work order to Leo

## Autonomy Value
**Replaces:** Broker manually checking GHL for new leads.
**Result:** Every lead processed, scored, and routed within 15 minutes of form submission. Zero leads sitting unprocessed.
**Advaita gap closed:** Lead intake automation — from 0% → 100% AI-autonomous.
