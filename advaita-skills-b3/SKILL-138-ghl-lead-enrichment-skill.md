# SKILL-138: GHL Lead Enrichment Automation
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Auto-enrich GHL contacts with web research, LinkedIn data, and business intel within minutes of lead creation.

## TRIGGER
New GHL contact created with email address.

## EXECUTION STEPS
1. Receive GHL webhook: new contact event
2. Pull contact: name, email, phone, source
3. Run Exa search: "[name] [company]" → find LinkedIn, website, press mentions
4. Extract:
   - Company (if B2B)
   - Role/title
   - Business type
   - Estimated company size
   - LinkedIn URL
5. Update GHL contact fields: company, job_title, linkedin_url, business_type
6. Add enrichment note: "Auto-enriched [timestamp] by Squirrel"
7. Log enrichment to Drive: `fki-ops/enrichment-log-[date].md` (append)
8. If enrichment score > 8: tag "high-intent" in GHL

## DIAMOND GATE
- T1: Public data only — no PII scraping ✅
- T2: File > 200 bytes ✅
- T3: GHL field updates REVERSIBLE ✅
