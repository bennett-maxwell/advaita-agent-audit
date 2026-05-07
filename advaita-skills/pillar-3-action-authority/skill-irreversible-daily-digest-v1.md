---
skill: irreversible-daily-digest
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI manages daily digest for irreversible decisions — Bennett reviews once, AI executes approved items
---
# Irreversible Action Daily Digest Skill v1

## Purpose
All IRREVERSIBLE actions accumulate in a daily digest. Bennett reviews once per day (ideally morning), approves/rejects, and AI executes approved items immediately.

## Digest File Location
`~/.openclaw/workspace/daily-digest.md` (local) + Drive backup at FKI Skills folder.

## Digest Entry Format
```
## DIGEST-[YYYYMMDD]-[NNN]
**Time logged**: [timestamp MDT]
**Action**: [specific action — 1 sentence]
**Why**: [business reason — 1 sentence]
**Impact if approved**: [what happens]
**Impact if not approved**: [what's skipped]
**Deadline**: [date/time this decision expires if any]
**Status**: PENDING / APPROVED / REJECTED / EXPIRED
```

## Digest Categories (sorted for fast review)
1. HIGH PRIORITY (time-sensitive, expires in <24h)
2. STANDARD (standard review window)
3. DEFERRED (no deadline, can wait)

## Digest Delivery
Daily digest compiled and posted to #leo-auto at 6:00 AM MDT as Slack message.
Bennett replies "approve [NNN]" or "reject [NNN]" → Squirrel executes or archives.

## After Approval
AI executes immediately, posts receipt to #leo-auto with timestamp.
Archives approved item with execution confirmation.

## Autonomy Value
**Replaces:** Bennett making ad hoc decisions throughout the day on individual requests.
**Result:** One daily 5-minute review session replaces constant interruptions. AI queues everything, Bennett approves in batch.
**Advaita gap closed:** Irreversible decision management — from 0% → systematic AI-managed batch review.
