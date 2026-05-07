---
skill: gap-analysis-execution
pillar: continuous-improvement
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI identifies its own capability gaps — proactively requests new skills it needs
---
# Gap Analysis Execution Skill v1

## Purpose
Systematically identify where FKI operations are NOT yet AI-autonomous and generate a prioritized list of skills or capabilities needed to close those gaps.

## Gap Detection Methods

**Method 1: Task Failure Analysis**
Review ERRORS.md for recurring patterns where AI could not complete tasks.
Each recurring failure = a gap in capability or skill coverage.

**Method 2: Human Gate Analysis**
Review human gate triggers from last 30 days.
Each human gate that didn't NEED to be human → skill/capability to build.
Each human gate that DID need to be human → refine gate criteria.

**Method 3: Work Order Analysis**
Review all work orders sent to Leo/Ivan in last 30 days.
Work orders that could have been handled by Squirrel with better skills → skill gaps.

**Method 4: Advaita Completion Scoring**
For each FKI business function:
Score 0–100% AI-autonomous.
Any function below 80% → gap candidate.

## Output: Prioritized Gap List
```
GAP-[NNN]: [Business function]
Current autonomy: X%
Gap description: [what AI can't do yet]
Impact: HIGH/MEDIUM/LOW (revenue or time impact)
Skill needed: [proposed new skill or capability]
Priority: P1/P2/P3
```

## Monthly Gap Report
Full gap list posted to #leo-auto on 1st of each month.
P1 gaps → immediate new skill creation.
P2 gaps → queued in Sprint Board.

## Autonomy Value
**Replaces:** Waiting for failures to reveal gaps.
**Result:** Gaps proactively identified and queued before they become failures. Advaita completion % increases systematically.
**Advaita gap closed:** Self-improvement intelligence — from 0% → 90% systematic.
