# SKILL-193: Data Quality Monitor
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor FKI data quality across all connected systems. Bad data = bad decisions. Keep all sources clean and synced.

## TRIGGER
Daily 4 AM MDT (auto).

## EXECUTION STEPS
1. Check GHL data quality:
   - Contacts with no email (> 10%: flag)
   - Contacts with duplicate phone numbers
   - Pipeline stages with 0-activity > 60d
2. Check QB data quality:
   - Revenue entries without GHL contact match
   - Expense categories uncategorized > 5%
   - Bank reconciliation overdue > 7d
3. Check Meta Ads API:
   - Campaigns with no conversion events (pixel not firing?)
   - Attribution window mismatches
4. Check Drive:
   - Stale skill files > 180d not accessed (log for review)
5. Compile data quality score per system (0-100%)
6. Flag: any system < 80% quality
7. Upload report to Drive: `fki-intelligence/data-quality-[date].md`
8. Post daily scores to #leo-auto

## DIAMOND GATE
- T1: Quality metrics only ✅
- T2: File > 200 bytes ✅
- T3: Monitoring only — no auto-corrections ✅
