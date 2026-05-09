# SKILL-149: Team Performance Review Automation
**Version:** 1.0 | **Pillar:** Advanced Systems | **Reversibility:** REVERSIBLE

## PURPOSE
Monthly automated performance summary for FKI team members. Objective metrics compiled without manager input required.

## TRIGGER
Monthly 28th at 5 PM MDT (auto) OR Bennett says "performance review [name]".

## EXECUTION STEPS
1. Pull objective metrics per team member (from source systems):
   - Leo: tasks completed vs assigned (from Notion sprint board)
   - Marketing: campaign ROAS delivered (Meta API)
   - Coaching: NPS scores for assigned clients (GHL)
   - Sales: close rate + pipeline managed (GHL)
2. Compare to role targets (from Drive: `fki-ops/role-targets.md`)
3. Generate performance summary:
   - Top 3 wins
   - Top 1-2 development areas
   - Objective score vs target (no subjective ratings)
4. Upload to Drive: `fki-ops/performance/[name]-[month]-[year].md`
5. Post team aggregate (no individual names) to #leo-auto

## DIAMOND GATE
- T1: Objective metrics only — no subjective performance claims ✅
- T2: File > 200 bytes ✅
- T3: Report only — no automated HR actions ✅
