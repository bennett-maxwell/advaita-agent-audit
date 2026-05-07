---
skill: daily-digest-compilation
pillar: coordination
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI compiles and delivers daily digest — irreversible decisions organized for 5-min Bennett review
---
# Daily Digest Compilation Skill v1

## Purpose
At 6:00 AM MDT every day, AI compiles all queued IRREVERSIBLE actions into a structured digest and posts to #leo-auto for Bennett's review. One 5-minute session replaces constant interruptions.

## Digest Compilation Process

**Step 1**: Pull all entries from daily-digest.md with status PENDING
**Step 2**: Sort by: HIGH PRIORITY first, then STANDARD, then DEFERRED
**Step 3**: Check for EXPIRED items (past deadline) → mark EXPIRED, alert
**Step 4**: Format for Slack delivery

## Digest Slack Format
```
📋 DAILY DIGEST — [Date] 6:00 AM MDT
Squirrel has [N] items awaiting your review.

🔴 HIGH PRIORITY ([N] items):
[NNN] [Action] — [Why] — expires [time]

🟡 STANDARD ([N] items):
[NNN] [Action] — [Why]

⚫ DEFERRED ([N] items):
[NNN] [Action] — [Why] — no deadline

Reply "approve [NNN]" or "reject [NNN]"
To approve all standard: "approve all standard"
```

## Response Processing
When Bennett replies to digest:
- "approve [NNN]" → AI executes that specific item → posts receipt
- "reject [NNN]" → archives item as rejected → no action
- "approve all standard" → AI executes all STANDARD items → posts batch receipt
- No response by 6 PM MDT → items remain PENDING, re-queued tomorrow

## Autonomy Value
**Replaces:** Random interruptions throughout the day for approval of non-urgent items.
**Result:** Bennett's decision load is batched to one 5-minute session. All decisions made. Nothing blocked.
**Advaita gap closed:** Decision workflow efficiency — from 0% → 100% structured.
