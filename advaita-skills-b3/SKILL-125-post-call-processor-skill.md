# SKILL-125: Post-Call Processor Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Process Plaud recordings from Bennett's calls. Extract action items, update GHL, log notes, trigger follow-up sequences automatically.

## TRIGGER
Plaud transcript uploaded to Drive folder `fki-plaud/raw-transcripts/`.

## EXECUTION STEPS
1. Detect new transcript in Drive folder (check every 30 min)
2. Read transcript using Plaud Transcript Intelligence (SKILL-7 from FKI-SKILL.md)
3. Extract:
   - Client name + call type
   - Key discussion points (3-5 bullets)
   - Action items (who / what / when)
   - Promises made by Bennett
   - Red flags or concerns raised
4. Update GHL contact note with summary
5. For each Bennett action item: create GHL task with due date
6. If follow-up email promised: draft and queue in GHL
7. Log processed transcript to Drive: `fki-coaching/session-notes/[name]-[date].md`
8. Post action item list to #leo-auto

## DIAMOND GATE
- T1: No coaching outcome claims in notes ✅
- T2: File > 200 bytes ✅
- T3: GHL tasks + queued emails REVERSIBLE ✅
