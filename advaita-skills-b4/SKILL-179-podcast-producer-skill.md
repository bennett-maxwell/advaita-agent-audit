# SKILL-179: Podcast Production Automation
**Version:** 1.0 | **Pillar:** AI Marketing Content | **Reversibility:** REVERSIBLE

## PURPOSE
Full podcast episode production automation: guest research, interview questions, show notes, clip timestamps, social distribution snippets.

## TRIGGER
Bennett books podcast guest (calendar event with "podcast" in title).

## EXECUTION STEPS
1. Pull guest name from calendar event
2. Run Exa research: guest background, recent work, talking points, controversies to avoid
3. Run bennett-intelligence-layer-skill: episode angle matching brand narrative
4. Generate:
   - Guest bio (150 words)
   - 15 interview questions (opener, main 10, closer 4)
   - Episode title + 3 alt titles
   - Show notes template (ready for transcript fill)
   - Social clips strategy (5 clip moments to pull post-recording)
5. Upload episode brief to Drive: `fki-content/podcast/[guest-name]-[date].md`
6. Send brief to Bennett via SMS 2h before recording
7. Post to #leo-auto: guest + episode angle + recording date

## DIAMOND GATE
- T1: Guest research from public sources only ✅
- T2: File > 200 bytes ✅
- T3: Brief document — no financial actions ✅
