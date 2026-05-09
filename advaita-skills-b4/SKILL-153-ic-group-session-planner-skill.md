# SKILL-153: IC Group Session Planner
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-generate weekly group coaching session plans for IC cohorts. Skill-matched drills, game scenarios, and debrief frameworks.

## TRIGGER
Weekly Friday 5 PM MDT (auto) for following week sessions.

## EXECUTION STEPS
1. Pull current IC cohort from GHL (tag: ic-enrolled, active)
2. Aggregate skill levels (from last assessments)
3. Load IC session library from Drive: `fki-ic/session-library.md`
4. Generate 3 session plans (Mon/Wed/Fri or per schedule):
   - Warm-up (10 min)
   - Skill drill block (20 min) — level-matched
   - Scenario play (20 min) — game-situation focus
   - Round-robin games (30 min)
   - Debrief (10 min) — coaching cues
5. Upload weekly plan to Drive: `fki-ic/session-plans/week-[date].md`
6. Post plan link to #leo-auto (Leo distributes to coaches)

## DIAMOND GATE
- T1: No outcome claims in session plans ✅
- T2: File > 200 bytes ✅
- T3: Plans document only ✅
