# SKILL-197: Weekly Ops Orchestrator
**Version:** 1.0 | **Pillar:** Autonomy Glue | **Reversibility:** REVERSIBLE

## PURPOSE
Master weekly automation sequence. Every Sunday-Monday the machine resets, reviews, and plans. Bennett focuses on calls and closes.

## TRIGGER
Sunday 9:00 PM MDT (auto) — runs overnight for Monday morning delivery.

## EXECUTION SEQUENCE
SUNDAY NIGHT:
1. SKILL-109: Audience Segmentation
2. SKILL-140: GHL Pipeline Cleanup
3. SKILL-145: GHL Tag Taxonomy Enforcement
4. SKILL-105: Content Calendar (next week)
5. SKILL-153: IC Group Session Planner

MONDAY MORNING (7:00 AM):
6. SKILL-147: Weekly KPI Digest
7. SKILL-137: Weekly P&L
8. SKILL-191: Market Intelligence
9. SKILL-148: AI Meeting Prep (Monday's calls)

## OUTPUT
- Weekly KPI digest in #leo-auto by 7:30 AM Monday
- Content calendar ready in Drive
- GHL cleaned and segmented
- Bennett has full context before first call

## DIAMOND GATE
- T1: Aggregate of compliant skills ✅
- T2: File > 200 bytes ✅
- T3: All constituent skills REVERSIBLE ✅
