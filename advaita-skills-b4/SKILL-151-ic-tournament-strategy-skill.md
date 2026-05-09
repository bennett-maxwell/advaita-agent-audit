# SKILL-151: IC Tournament Strategy Automation
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Generate tournament preparation strategies and competitive playbooks for IC (Illegal Civilizations) pickleball coaching clients.

## TRIGGER
Bennett says "IC tournament prep [client name]" OR client books tournament prep session in GHL.

## EXECUTION STEPS
1. Pull client profile from GHL: skill level, tournament history, physical notes
2. Load IC competitive framework from Drive: `fki-ic/tournament-framework.md`
3. Run bennett-intelligence-layer-skill for current IC coaching narrative
4. Generate personalized tournament playbook:
   - 4-week pre-tournament training block (drills + matches + fitness)
   - Mental game protocol (visualization, routine, pressure handling)
   - Match strategy by opponent archetype (bangers / dinkers / speedups)
   - Equipment checklist
   - Day-of routine (warm-up, warm-down, between games)
5. Add disclaimer: "Individual performance results will vary based on physical conditioning, competition level, and consistency of practice."
6. Upload to Drive: `fki-ic/client-playbooks/[client-id]-tournament-[date].md`
7. Post receipt to #leo-auto

## DIAMOND GATE
- T1: Performance disclaimer on all competitive outcomes ✅
- T2: File > 200 bytes ✅
- T3: Document only ✅
