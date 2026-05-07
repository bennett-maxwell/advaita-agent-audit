---
skill: legal-compliance-gate
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI enforces all legal/compliance rules automatically — zero legal violations without human review
---
# Legal Compliance Gate Skill v1

## Purpose
Hard-stop enforcement of all FKI legal and compliance requirements. AI runs this check on EVERY content creation, communication draft, and public-facing material before any output is finalized.

## Compliance Checklist (run in order — fail any = STOP)

**STEP 1 — Banned Entity Check**
AI maintains an internal list of entity names that must never appear in any AI-generated content.
Source: FKI-SKILL.md Preflight Skill section, loaded at runtime.
Method: regex scan over full content before output.
Result: ANY match → REJECT output immediately. Log to compliance record.

**STEP 2 — Financial Figure Check**
Scan for: any dollar amount, percentage, income figure, revenue figure.
For each: verify FDD qualifier present in surrounding context (plus/minus 300 characters).
Required qualifier language: "per FDD Item [X]" OR "results may vary; see FDD" OR "illustrative; actual results vary" OR "consult your FDD and advisors."
Result: Missing qualifier → INSERT qualifier OR reject if context cannot be amended.

**STEP 3 — State Block Check**
For any content mentioning IC + target state: block if state is on IC blocked list.
For any content mentioning SH + target state: block if state is on SH blocked list.
Blocked state lists are loaded from FKI-SKILL.md Preflight Skill at runtime.
Result: State block triggered → REMOVE brand from content OR flag for human review.

**STEP 4 — Brand Language Check**
IC mentions: verify "community hub" language (not the incorrect alternative term).
SH mentions: verify SBA-friendly language (SH is SBA-approved).
SRP mentions: verify photography/memory-making language.

**STEP 5 — Forward-Looking Language Check**
Scan for: "you will earn," "you will make," "guaranteed," "certain to," "will generate."
Result: Any forward-looking income claim → REPLACE with FDD-qualified language or REJECT.

## Compliance Log
Every check logged to Drive compliance record: date, content type, check result, action taken.

## Runtime Loading Note
The specific banned term list and state block registry are loaded from FKI-SKILL.md at runtime — not hardcoded in this skill to avoid propagation of banned terms through skill files.

## Autonomy Value
**Replaces:** Manual content review for legal compliance.
**Result:** Zero compliance violations in AI-generated content. Legal risk eliminated at the source.
**Advaita gap closed:** Content compliance enforcement — from 0% → 100% AI-autonomous.
