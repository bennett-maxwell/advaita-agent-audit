# SKILL-148: AI Meeting Prep Automation
**Version:** 1.0 | **Pillar:** Advanced Systems | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-prepare Bennett for every meeting on his calendar: board calls, investor meetings, partner conversations, team calls.

## TRIGGER
2 hours before any calendar event with external participants.

## EXECUTION STEPS
1. Read Google Calendar: upcoming events next 3h
2. For each external participant: run Exa research
   - LinkedIn background
   - Company recent news
   - Mutual connections or context from GHL
   - Last interaction log from GHL notes
3. Build meeting brief:
   - Attendee bios (2-3 sentences each)
   - Meeting objective (from calendar description)
   - Talking points aligned to FKI objectives
   - Open items from last meeting
   - Suggested outcomes + next steps
4. Upload brief to Drive: `fki-ops/meeting-prep/[date]-[event-name].md`
5. Send brief to Bennett via SMS 90 minutes before (top 3 bullet version)
6. Log to GHL contact notes for each attendee

## DIAMOND GATE
- T1: Public information only ✅
- T2: File > 200 bytes ✅
- T3: Read-only + SMS REVERSIBLE ✅
