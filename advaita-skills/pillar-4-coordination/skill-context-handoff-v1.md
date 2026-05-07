---
skill: context-handoff-on-session-end
pillar: coordination
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI saves context before session ends — next session picks up exactly where last one left off
---
# Context Handoff Skill v1

## Purpose
Before any long session ends (or when approaching context limit), AI saves critical context to persistent storage. Next session resumes with full context, no re-briefing needed.

## Context Save Trigger
- Thread approaching 80% context length
- Session ending by user signal
- Batch of significant work completed
- Any multi-session project reaching a milestone

## Context to Save (to Thread Context Doc — cmov2m7wc0es107adncup49df)

**Active Projects**: What's in flight, current status, next action
**Key Decisions Made**: Any choices made this session (approach, priority, etc.)
**Pending Work Orders**: Open Leo/Ivan tasks and their expected SLA
**Numbers Discovered**: Any specific figures, IDs, timestamps that must persist
**Blockers**: Anything paused and why
**Next Actions**: Ordered list of what to do next session

## Save Format (to Plan Overview section)
```
SESSION HANDOFF — [timestamp]
Context: [what was being done]
Status: [current state]
Pending: [open items]
Numbers: [key figures — file IDs, SHAs, etc.]
Next: [ordered next steps]
```

## Pickup Protocol (next session)
First action of any new session: ReadDocument(cmov2m7wc0es107adncup49df) → ingest context → resume from Next Actions list.

## Autonomy Value
**Replaces:** Squirrel starting each session from scratch, re-learning context.
**Result:** Continuous execution across sessions. Multi-day projects flow without interruption.
**Advaita gap closed:** Multi-session continuity — from 0% → 100% systematic.
