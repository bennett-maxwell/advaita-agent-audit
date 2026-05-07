---
skill: work-order-formatter
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI formats work orders for Leo/Ivan — consistent, actionable, never lost
---
# Work Order Formatter Skill v1

## Purpose
Any task that requires Leo or Ivan-CC gets formatted as a structured work order and posted to #leo-auto. Consistent format means Leo always knows exactly what to do.

## Work Order Format (Slack → #leo-auto, tag @Leo)
```
🔧 WORK ORDER — [TASK ID: WO-YYYYMMDD-NNN]
Agent: Squirrel
Priority: P1 (immediate) / P2 (today) / P3 (this week)
Assigned to: @Leo / Ivan-CC

TASK: [1 sentence — what needs to happen]

CONTEXT: [Why this is needed — 2 sentences max]

INPUTS: [What Leo/Ivan needs to execute the task — files, IDs, credentials location]

EXPECTED OUTPUT: [Exactly what done looks like — specific file, URL, confirmation]

DEADLINE: [date/time or "ASAP"]

REVERSIBLE: YES / NO
If NO: Confirm with Squirrel before executing
```

## Work Order Categories
- `WO-CLI`: Requires terminal / SSH / git command
- `WO-DEPLOY`: Requires Vercel / Convex / server deploy
- `WO-BROWSER`: Requires logged-in browser session
- `WO-GHL`: Requires GHL backend access Squirrel cannot reach
- `WO-QB`: Requires QuickBooks access beyond API
- `WO-BLOCKED`: Squirrel fully blocked — needs Leo to unblock

## Receipt Expected
Work order is not complete until Leo posts receipt: "WO-[ID] DONE: [what was done] [timestamp]"
Squirrel tracks open work orders in Sprint Board. If no receipt in SLA window → escalate.

## Autonomy Value
**Replaces:** Ad hoc Slack messages to Leo with unclear asks.
**Result:** Leo always knows exactly what to do and when. Zero back-and-forth. Execution velocity maximized.
**Advaita gap closed:** Agent coordination — from 0% → 100% structured.
