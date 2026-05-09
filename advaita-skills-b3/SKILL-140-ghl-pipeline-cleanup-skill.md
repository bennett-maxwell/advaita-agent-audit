# SKILL-140: GHL Pipeline Cleanup Automation
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Weekly GHL pipeline hygiene. Move stale leads, remove duplicates, update stages, flag ghosted prospects.

## TRIGGER
Weekly Sunday 10 PM MDT (auto).

## EXECUTION STEPS
1. Pull all GHL contacts: last_modified date + pipeline stage
2. Flag stale by rule:
   - In "lead" stage > 30d without activity → move to "nurture"
   - In "booked" stage > 7d without call note → move to "no-show"
   - In "proposal" stage > 21d → flag "ghosted"
3. Deduplicate: find contacts with same email or phone → merge (keep newest data)
4. Update GHL pipeline stages via API
5. Generate cleanup report:
   - Contacts moved
   - Duplicates merged
   - Ghosted count
6. Upload to Drive: `fki-ops/pipeline-cleanup-[date].md`
7. Post summary to #leo-auto

## DIAMOND GATE
- T1: No claims about pipeline performance ✅
- T2: File > 200 bytes ✅
- T3: Stage moves REVERSIBLE ✅
