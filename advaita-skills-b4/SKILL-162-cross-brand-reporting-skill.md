# SKILL-162: Cross-Brand Reporting Automation
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Unified monthly cross-brand performance report. IC vs SH vs SRP comparison. Board-ready format.

## TRIGGER
Monthly 1st 8 AM MDT (auto) OR Bennett says "monthly brand report".

## EXECUTION STEPS
1. Pull for each brand (IC, SH, SRP):
   - Revenue MTD (QB)
   - New clients enrolled (GHL)
   - Active clients (GHL)
   - Churn rate (GHL)
   - Meta ROAS (Meta Ads API)
   - CAC (spend / enrollments)
   - NPS average (GHL survey data)
2. Build comparison table: all 8 metrics × 3 brands
3. Delta vs prior month
4. Narrative summary: top performer, biggest mover, flag for attention
5. Upload to Drive: `fki-reports/cross-brand-[month]-[year].md`
6. Post to #leo-auto

## DIAMOND GATE
- T1: Actuals from source APIs only ✅
- T2: File > 200 bytes ✅
- T3: Report only ✅
