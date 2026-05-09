# SKILL-141: GHL Dead Lead Revival Automation
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Systematic re-engagement of GHL contacts who went cold 30-180 days ago. Multi-touch revival sequence without manual outreach.

## TRIGGER
Weekly Thursday 9 AM MDT (auto).

## EXECUTION STEPS
1. Pull GHL contacts: last_modified 30-180d ago, no active pipeline stage
2. Segment by cold duration:
   - 30-60d cold: soft re-engagement ("checking in" style)
   - 60-120d cold: new angle (different offer/pain point)
   - 120-180d cold: breakup email ("closing your file")
3. For each segment: generate personalized revival email using bennett-intelligence-layer-skill
4. Add FDD qualifiers if offer mentioned
5. Queue in GHL (NOT sent — Leo review required for each batch)
6. Log revival list to Drive: `fki-ops/dead-lead-revival-[date].md`
7. Post revival queue size to #leo-auto for Leo activation

## DIAMOND GATE
- T1: FDD qualifiers on offers ✅
- T2: File > 200 bytes ✅
- T3: Queued not sent — Leo activates ✅
