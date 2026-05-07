---
skill: skill-effectiveness-measurement
pillar: continuous-improvement
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI measures which skills are actually working — removes guessing from capability management
---
# Skill Effectiveness Measurement Skill v1

## Purpose
Track which skills are making a measurable difference and which are unused or ineffective. Invest in what works; deprecate what doesn't.

## Effectiveness Metrics (per skill)

**Usage Rate**: Times invoked per week (from audit trail)
**Success Rate**: % of invocations that completed successfully (from audit trail)
**Impact Score**: AI's assessment of business impact (HIGH/MEDIUM/LOW)
- HIGH: Directly replaced a human action (time saved = billable hours freed)
- MEDIUM: Reduced time on task but still required human review
- LOW: Rarely used or human still does same work

**Error Rate**: % of invocations requiring retry or escalation

## Monthly Effectiveness Report
```
SKILL EFFECTIVENESS REPORT — [Month]

TOP 5 MOST IMPACTFUL:
1. [Skill] — [usage] invocations, [impact], [time saved estimate]

UNDERPERFORMING (review or deprecate):
1. [Skill] — 0 invocations in 30 days
2. [Skill] — 80% error rate

RECOMMENDED IMPROVEMENTS:
1. [Skill] — [specific improvement needed]
```

## Deprecation Process
Skill with 0 usage in 60 days + no planned future use → deprecation proposal to Bennett digest.
Bennett approves → archive skill file + GitHub commit noting deprecation.

## Autonomy Value
**Replaces:** Guessing which AI capabilities are valuable.
**Result:** FKI's skill investment is always concentrated in highest-impact areas. ROI of AI autonomy is measurable.
**Advaita gap closed:** AI capability ROI measurement — from 0% → 90% systematic.
