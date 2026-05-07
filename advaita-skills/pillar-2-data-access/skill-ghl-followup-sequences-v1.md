---
skill: ghl-followup-sequences
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI manages follow-up sequence enrollment — every candidate gets the right content at the right time
---
# GHL Follow-Up Sequence Manager Skill v1

## Purpose
Automatically enroll and unenroll candidates in the correct GHL follow-up sequences based on their current stage, tag, and behavioral signals.

## Sequence Library

**SEQ-001: New Lead Welcome**
Trigger: `ai-qualified` tag applied
Content: Welcome + FKI process overview + calendar link to schedule discovery call
Duration: 7 days, 3 touchpoints

**SEQ-002: Nurture — Capital**
Trigger: `ai-nurture-capital` tag applied
Content: Funding path education series (ROBS, SBA, HELOC — general info, consult financial advisor)
Duration: 90 days, 6 touchpoints

**SEQ-003: Nurture — Timeline**
Trigger: `ai-nurture-timeline` tag applied
Content: Franchise education series, territory urgency, seasonal re-engagement
Duration: 180 days, 8 touchpoints

**SEQ-004: Pre-Discovery Education**
Trigger: Discovery call scheduled (calendar)
Content: What to expect on discovery call, franchise process overview
Duration: Until call date

**SEQ-005: Post-Discovery**
Trigger: Stage → Post-Discovery
Content: Top brand summaries, FDD intro, validation call preparation
Duration: 14 days or until FDD requested

**SEQ-006: FDD Companion**
Trigger: FDD sent
Content: FDD synthesis highlights, suggested questions for attorney, validation call prep
Duration: 21 days or until validation complete

**SEQ-007: Re-Engagement**
Trigger: `pipeline-stalled` or dormant >30 days
Content: Educational content, territory update, "is now the right time?" check-in

## Enrollment/Unenrollment Rules
Unenroll from any sequence immediately when: candidate advances stage, responds directly, marks as not interested.
Never enroll in 2 conflicting sequences simultaneously.

## Autonomy Value
**Replaces:** Broker manually triggering emails and forgetting follow-ups.
**Result:** Zero candidates fall through the cracks. Every touchpoint delivered at optimal time.
**Advaita gap closed:** Follow-up automation — from 0% → 100% AI-autonomous.
