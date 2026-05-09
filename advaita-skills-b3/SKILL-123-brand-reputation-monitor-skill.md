# SKILL-123: Brand Reputation Monitor
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor FKI brand mentions across web, social, and review sites. Flag negative mentions. Surface PR opportunities.

## TRIGGER
Daily 6 AM MDT (auto).

## EXECUTION STEPS
1. Run Exa search for brand mentions (last 24h):
   - "Illegal Civilizations" + "Bennett Maxwell" + "IC pickleball"
   - "Smash Hotel" + "SH coaching"
   - "Sports Retail Pro" + "SRP franchise"
2. Classify each mention: positive / neutral / negative / crisis
3. Score crisis risk: 1 (low) to 5 (high)
4. Score 4-5: immediately post to #leo-auto with full context
5. Draft response for negative mentions (not posted — Leo review)
6. Log all mentions to Drive: `fki-brand/reputation-log-[date].md`
7. Weekly: trend report to #leo-auto

## DIAMOND GATE
- T1: No claims about brand perception ✅
- T2: File > 200 bytes ✅
- T3: Monitor only. Responses drafted not posted ✅
