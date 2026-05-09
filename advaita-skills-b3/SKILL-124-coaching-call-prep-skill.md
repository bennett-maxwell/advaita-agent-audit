# SKILL-124: Coaching Call Prep Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-prepare Bennett for every coaching call. Pulls client history, last session notes, outstanding issues, and suggested focus areas.

## TRIGGER
60 minutes before any coaching call on Bennett's Google Calendar.

## EXECUTION STEPS
1. Read Google Calendar for upcoming calls (next 2 hours)
2. For each call: extract client name from event
3. Pull from GHL: enrollment date, pipeline stage, last contact, notes
4. Pull from Drive: last session notes (fki-coaching/session-notes/[name])
5. Pull Plaud transcript summary if available (last 7d)
6. Generate 1-page prep brief:
   - Client snapshot (LTV, cohort week, risk level)
   - Last session key points
   - Suggested focus areas for this call
   - Open questions / action items
7. Send brief to Bennett's phone via SMS (via GHL) 30 min before call
8. Log prep sent to Drive: `fki-coaching/prep-logs/[date]-[name].md`

## DIAMOND GATE
- T1: No outcome predictions ✅
- T2: File > 200 bytes ✅
- T3: Read-only + SMS send REVERSIBLE ✅
