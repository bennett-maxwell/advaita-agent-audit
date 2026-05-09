# SKILL-191: Market Intelligence Monitor
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Weekly market intelligence briefing for Bennett. Industry trends, regulatory changes, competitor moves, opportunity signals.

## TRIGGER
Weekly Friday 4 PM MDT (auto).

## EXECUTION STEPS
1. Run Exa research (last 7 days):
   - Pickleball / sports retail / sports coaching industry news
   - Franchise regulation changes (FTC, state-level)
   - Competitor announcements (IC, SH, SRP competitors)
   - Social media trends in FKI verticals
   - Digital advertising cost trends (Meta/Google CPL shifts)
2. Score each finding: relevance (1-5) × urgency (1-5) = priority score
3. Top 10 findings by priority score
4. Generate 1-page intelligence brief:
   - Opportunities (act within 30d)
   - Threats (monitor or defend)
   - Trends (incorporate into 90d planning)
5. Upload to Drive: `fki-intelligence/market-brief-[date].md`
6. Post top 3 findings to #leo-auto

## DIAMOND GATE
- T1: External research cited, not invented ✅
- T2: File > 200 bytes ✅
- T3: Research document ✅
