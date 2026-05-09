# SKILL-155: SH Curriculum Update Automation
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor SH coaching curriculum for outdated content. Trigger update alerts when market conditions change or client feedback indicates gaps.

## TRIGGER
Monthly 15th (auto) OR Bennett says "SH curriculum review".

## EXECUTION STEPS
1. Pull SH curriculum outline from Drive: `fki-sh/curriculum-v[current].md`
2. Pull NPS feedback comments from last 30d (GHL survey data)
3. Run Exa research: sports hospitality industry trends (last 30d)
4. Run bennett-intelligence-layer-skill: check if curriculum reflects current narrative
5. Identify gaps:
   - Topics mentioned in negative NPS feedback
   - Industry developments not covered
   - Modules rated lowest by clients
6. Generate curriculum update brief:
   - Modules to retire (score < 6/10 + not core)
   - Modules to update (outdated info)
   - New modules to add (market gap)
7. Upload brief to Drive: `fki-sh/curriculum-reviews/review-[date].md`
8. Post to #leo-auto: gap count + highest priority updates

## DIAMOND GATE
- T1: Research only — no curriculum performance claims ✅
- T2: File > 200 bytes ✅
- T3: Recommendations only — no auto-update ✅
