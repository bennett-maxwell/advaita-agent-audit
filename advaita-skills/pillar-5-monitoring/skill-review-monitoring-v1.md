---
skill: review-monitoring
pillar: monitoring
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI monitors Google/Yelp reviews for FKI — reputation management on autopilot
---
# Review Monitoring Skill v1

## Purpose
Weekly automated check of FKI's Google Business Profile and Yelp reviews. New reviews surfaced immediately. AI drafts response recommendations.

## Monitored Profiles
- FranchiseKI Google Business Profile
- FKI Yelp Business Profile
- IC/SH/SRP Google profiles (for brand reputation signals)

## Alert Triggers (REVERSIBLE — monitoring only)

**New 5-Star Review**: Post to #leo-auto with: review content + suggested response draft + "ACTION: Bennett/broker to respond within 48h"

**New 3-Star or Below Review**: POST IMMEDIATELY to #leo-auto with: review content + AI analysis of concern + suggested response draft + "URGENT: Respond within 24h. This review is public."

**Review Pattern**: If 2+ negative reviews in 30 days on same topic → trend alert with root cause hypothesis.

## Response Draft Format (AI-generated, human review required before posting — IRREVERSIBLE)
```
REVIEW RESPONSE DRAFT:
[Polite acknowledgment] + [Specific response to concern] + [Invitation to connect directly]
NOTE: Review response posting = IRREVERSIBLE (public, indexed). Queued to daily digest for Bennett approval.
```

## Autonomy Value
**Replaces:** Forgetting to check reviews for weeks.
**Result:** Every review seen within 24h. Responses drafted. Reputation actively managed.
**Advaita gap closed:** Reputation monitoring — from 0% → 100% AI-autonomous (response posting requires Bennett approval).
