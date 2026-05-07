---
skill: slack-receipt-formatter
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI formats receipts consistently — Bennett and Leo always get the same clear format
---
# Slack Receipt Formatter Skill v1

## Purpose
Every Squirrel task completion posts a formatted receipt to #leo-auto. Consistent format = fast human review. No receipt = task didn't happen.

## Receipt Format (post to C0AKXT2S1T2 #leo-auto)
```
✅ SQUIRREL RECEIPT — [TASK NAME]
Date: [YYYY-MM-DD HH:MM MDT]
Agent: Squirrel (autonomous)

WHAT WAS DONE:
• [Bullet 1 — specific action taken]
• [Bullet 2 — specific action taken]
• [Bullet 3 — if applicable]

SOURCE DATA USED: [where data came from + timestamp]

OUTPUT / ARTIFACTS:
• [GitHub SHA if commit] / [Drive file ID if Drive save] / [Notion URL if Notion update]

VERIFIED BY: [how completion was confirmed — file exists, SHA returned, etc.]

DIAMOND: T1✓ T2✓ T3✓ REVERSIBLE
```

## Receipt Timing
Post AFTER verification of output, not before or during.
Never post receipt for work that isn't confirmed done.

## Receipt for IRREVERSIBLE Items Queued
```
📋 DIGEST ENTRY ADDED — [TASK NAME]
Item queued for Bennett review. Not executed.
Digest: daily-digest.md [timestamp]
```

## Escalation Receipt
```
🚧 BLOCKED — [TASK NAME]
What failed: [specific error]
Steps attempted: [DIY skill steps 1–9]
Work order: WO-[ID] dispatched to @Leo
Status: Waiting on Leo/Ivan
```

## Autonomy Value
**Replaces:** Inconsistent status updates that require follow-up questions.
**Result:** Bennett and Leo always know exactly what happened, what was produced, and how to verify it.
**Advaita gap closed:** Communication discipline — from 0% → 100% standardized.
