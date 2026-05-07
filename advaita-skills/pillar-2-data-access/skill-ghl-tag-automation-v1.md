---
skill: ghl-tag-automation
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI manages GHL tags — candidate profile always current, segmentation always accurate
---
# GHL Tag Automation Skill v1

## Purpose
Maintain accurate, current tags on every GHL contact based on AI assessment and behavioral signals. Enables precise segmentation for sequences, reporting, and routing.

## Core Tag Taxonomy

**Qualification Tags**
- `ai-qualified` / `ai-nurture-capital` / `ai-nurture-timeline` / `ai-disqualify` / `ai-hold-info-needed`

**Score Tier Tags**
- `score-hot` (80+) / `score-warm` (60–79) / `score-developing` (40–59) / `score-cold` (<40)

**Brand Interest Tags**
- `interest-ic` / `interest-sh` / `interest-srp` / `interest-unknown`

**State Eligibility Tags** (applied automatically when state known)
- `eligible-ic` / `ineligible-ic` / `eligible-sh` / `ineligible-sh`

**Buyer Profile Tags**
- `profile-semi-absentee` / `profile-owner-operator` / `profile-investor` / `profile-multi-unit`
- `profile-military` / `profile-healthcare` / `profile-educator` / `profile-attorney`

**Pipeline Health Tags**
- `pipeline-healthy` / `pipeline-stalled` / `pipeline-at-risk` / `pipeline-paused`

**Readiness Tags**
- `readiness-5of5` / `readiness-4of5` / `readiness-developing` / `close-now-signal`

## Tag Update Triggers
Tags updated automatically when:
- AI re-scores candidate (after call, after FDD review, after validation)
- Stage changes
- Behavior signals detected (email engagement, visit activity)
- Time-based triggers (dormancy tags)

## Autonomy Value
**Replaces:** Broker manually adding/removing tags based on memory of each candidate.
**Result:** GHL segmentation is always 100% accurate. Every sequence, report, and routing decision uses real data.
**Advaita gap closed:** CRM segmentation accuracy — from 0% → 100% AI-autonomous.
