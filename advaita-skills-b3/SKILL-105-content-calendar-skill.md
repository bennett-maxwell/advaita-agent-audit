# SKILL-105: Content Calendar Generator
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-generate 30-day content calendar for FKI brand social channels. Posts mapped to offers, launches, and coaching cycles.

## TRIGGER
First of each month (auto) OR Bennett says "content calendar [brand]".

## EXECUTION STEPS
1. Pull FKI brand schedule from Drive: `fki-ops/brand-calendar.md`
2. Run bennett-intelligence-layer-skill to get current brand narrative
3. Generate 30 posts per channel (IG, TikTok, YouTube Shorts):
   - 40% education/value
   - 30% social proof / transformation
   - 20% offer/CTA
   - 10% behind the scenes
4. Map posts to current coaching cohort dates
5. FDD qualifier on any income/result claim
6. Export as CSV + Notion page
7. Upload to Drive: `fki-content/[brand]-calendar-[month]-[year].csv`
8. Post receipt to #leo-auto

## DIAMOND GATE
- T1: FDD qualifiers on all result-based content ✅
- T2: File > 200 bytes ✅
- T3: Calendar draft — no auto-posting ✅
