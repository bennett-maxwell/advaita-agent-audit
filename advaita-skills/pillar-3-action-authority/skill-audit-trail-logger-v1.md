---
skill: audit-trail-logger
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI maintains complete audit trail — every action logged, reversible, and attributable
---
# Audit Trail Logger Skill v1

## Purpose
Every significant Squirrel action is logged to a persistent audit trail. This enables: debugging when things go wrong, compliance documentation, and continuous improvement analysis.

## Audit Log Location
GitHub: `bennett-maxwell/advaita-agent-audit` → `audit-trail/` → `YYYY-MM/actions-YYYYMMDD.md`

## Log Entry Format
```
## ACT-[YYYYMMDD]-[NNN]
**Timestamp**: [ISO timestamp MDT]
**Agent**: Squirrel
**Thread/Session**: [context identifier]
**Action Type**: REVERSIBLE / IRREVERSIBLE / HUMAN-GATE
**Action**: [1-sentence description]
**Trigger**: [what caused this action — skill invocation, schedule, user request]
**Output**: [file ID, SHA, Slack ts, or "digest queued"]
**Verification**: [how completion was confirmed]
**Status**: COMPLETE / PENDING / FAILED / ESCALATED
```

## Daily Audit Commit
All audit entries for the day committed to GitHub at 11:59 PM MDT.
Commit message: `audit: daily action log [YYYY-MM-DD] [Squirrel autonomous]`

## Retention Policy
Audit logs retained indefinitely (GitHub history). Read-only after commit. Never delete audit entries.

## Usage
When debugging: search audit trail for action type and date.
When compliance review requested: pull specific date range from GitHub.
When improvement analysis needed: feed audit data to continuous improvement skill.

## Autonomy Value
**Replaces:** No formal record of what AI did.
**Result:** Complete, searchable, permanent record of every Squirrel action. Trust in AI autonomy is verifiable.
**Advaita gap closed:** AI accountability and auditability — from 0% → 100%.
