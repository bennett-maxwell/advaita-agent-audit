# SKILL-145: GHL Tag Taxonomy Enforcement
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Enforce consistent GHL contact tagging across FKI. Detect rogue tags, merge duplicates, maintain master taxonomy.

## TRIGGER
Weekly Saturday 11 PM MDT (auto).

## EXECUTION STEPS
1. Pull all unique tags in GHL system
2. Compare to master taxonomy from Drive: `fki-ops/ghl-tag-taxonomy.md`
3. Flag:
   - Tags not in master list (rogue tags)
   - Duplicate semantic tags (e.g., "hotlead" vs "hot-lead" vs "hot_lead")
   - Tags with < 5 contacts (possible typos)
4. Generate taxonomy cleanup recommendations
5. For rogue tags: post to #leo-auto for Leo to decide keep/delete/merge
6. Upload taxonomy report to Drive: `fki-ops/tag-audit-[date].md`
7. Do NOT auto-delete tags — Leo approval required

## DIAMOND GATE
- T1: No contact data claims ✅
- T2: File > 200 bytes ✅
- T3: Audit only — no auto-delete ✅
