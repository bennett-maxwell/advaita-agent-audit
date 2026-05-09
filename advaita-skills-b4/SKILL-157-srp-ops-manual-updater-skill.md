# SKILL-157: SRP Operations Manual Updater
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Keep SRP franchise operations manual current. Detect when SOPs become outdated. Draft updates for legal review.

## TRIGGER
Quarterly (Jan/Apr/Jul/Oct 1st) OR Bennett says "SRP ops manual review".

## EXECUTION STEPS
1. Pull current SRP ops manual from Drive: `fki-franchise/ops-manual-v[current].md`
2. Pull: franchisee FAQ log (last 90d), support tickets, GHL notes from franchise team
3. Identify SOPs that generated > 3 support tickets → likely unclear or outdated
4. Run Exa: sports retail industry regulatory changes (last 90d)
5. Draft updates for flagged SOPs
6. MANDATORY: flag all changes with "LEGAL REVIEW REQUIRED — FRANCHISE DOCUMENT"
7. Upload draft to Drive: `fki-franchise/ops-manual-drafts/ops-manual-update-[date].md`
8. Post to #leo-auto: # of SOPs flagged for update + Drive link

## COMPLIANCE
All franchise document changes require legal review before distribution to franchisees.

## DIAMOND GATE
- T1: Legal review flag mandatory ✅
- T2: File > 200 bytes ✅
- T3: Draft only — not distributed without Bennett legal gate ✅
