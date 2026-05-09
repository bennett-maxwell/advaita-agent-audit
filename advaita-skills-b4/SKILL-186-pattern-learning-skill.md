# SKILL-186: Pattern Learning Engine
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Extract repeating patterns from FKI operations data. Surface insights that improve future decisions. The "get smarter over time" engine.

## TRIGGER
Monthly 1st (auto).

## EXECUTION STEPS
1. Pull last 30d operational data:
   - Which GHL pipelines had highest conversion rates? (SKILL-140 data)
   - Which Meta campaigns had highest ROAS? (SKILL-102 data)
   - Which email subject lines had highest open rates?
   - Which lead sources produced highest LTV? (SKILL-134 data)
2. Identify top 3 patterns in each category
3. Translate patterns into operational recommendations:
   - "Leads from [source] close 2.3x faster → increase spend on this source"
   - "Subject lines with [pattern] outperform by 34% → update templates"
4. Update relevant Drive config files with learned preferences (reversible)
5. Upload learning report to Drive: `fki-intelligence/pattern-log-[date].md`
6. Post 3 key patterns to #leo-auto

## DIAMOND GATE
- T1: Pattern observations only — no guaranteed future performance claims ✅
- T2: File > 200 bytes ✅
- T3: Config updates REVERSIBLE ✅
