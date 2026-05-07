---
skill: notion-sprint-board-manager
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI manages Sprint Board automatically — project tracking without manual Notion updates
---
# Notion Sprint Board Manager Skill v1

## Purpose
Automatically create, update, and close Sprint Board rows in Notion for every active project thread. Bennett always has real-time visibility into what's in flight.

## Sprint Board: Notion DB `335cf5514fd3813488dec82a68622d7b`

## Auto-Create Row Triggers
- Any thread with 3+ exchanges on a project/decision/action
- Any skill execution that produces a deliverable
- Any work order dispatched to Leo or Ivan

## Row Schema
```
Title: [project name — 1 line]
Status: 🔴 Red (created) → 🟡 Yellow (in progress) → 🟢 Green (done) → ⚫ Black (cancelled)
Owner: Squirrel / Leo / Ivan / Bennett
Priority: P1 (urgent/blocking) / P2 (high) / P3 (standard)
Due Date: [ISO date]
Notes: [current status, blockers, next action]
```

## Auto-Update Triggers (REVERSIBLE)
- Status → Yellow: when AI starts working on it
- Status → Green: when deliverable confirmed (receipt posted, file saved, commit verified)
- Status → Black: when explicitly cancelled
- Notes: updated at each major milestone

## Weekly Board Cleanup (every Sunday 8 PM MDT)
- Close all Green rows older than 7 days (archive to completed)
- Flag any Red rows older than 72h without progress → escalate or cancel
- Generate weekly summary: X completed, X in progress, X overdue

## Autonomy Value
**Replaces:** Bennett manually checking in on projects and tasks.
**Result:** Sprint Board is always current. Bennett opens Notion and sees exactly what's happening.
**Advaita gap closed:** Project visibility and tracking — from 0% → 100% AI-autonomous.
