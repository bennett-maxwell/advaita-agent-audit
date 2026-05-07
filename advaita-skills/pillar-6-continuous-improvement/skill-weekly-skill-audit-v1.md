---
skill: weekly-skill-audit
pillar: continuous-improvement
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI audits its own skills weekly — self-improving system that gets better automatically
---
# Weekly Skill Audit Skill v1

## Purpose
Every week, AI audits all FKI skills for: effectiveness, usage, staleness, and gaps. The fleet continuously improves itself without Bennett directing improvements.

## Audit Dimensions

**1. Usage Frequency**
Which skills have been invoked in the last 7 days?
Skills with zero usage: was this expected (infrequent) or a sign the skill isn't being loaded?

**2. Effectiveness Signals**
Skills that resolved their stated objective → flag as EFFECTIVE
Skills that triggered workarounds or manual fallback → flag for review

**3. Staleness Check**
Skills with hardcoded data that may be stale (state block lists, brand data, territory info) → flag for human review
Skills not updated in >60 days → flag for review

**4. Gap Detection**
Actions that Squirrel attempted but had no skill for → candidate new skills
Repeated ad hoc solutions for the same problem → candidate for new skill formalization

## Weekly Skill Audit Report (#leo-auto, Sundays)
- Skills used this week: [count + names]
- Skills flagged for staleness: [list]
- Skills flagged for effectiveness review: [list]
- New skill candidates identified: [list with brief description]
- Skills proposed for deprecation: [list]

## Improvement Loop
Audit findings feed into: skill-gap-analysis-v1, skill-learning-extraction-v1, and new skill creation workflow.

## Autonomy Value
**Replaces:** Bennett or Squirrel noticing skills are out of date only when they fail.
**Result:** Skill infrastructure always current, effective, and growing. Self-improving AI system.
**Advaita gap closed:** Skill maintenance automation — from 0% → 90% AI-autonomous.
