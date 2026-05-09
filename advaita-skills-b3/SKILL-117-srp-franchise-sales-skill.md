# SKILL-117: SRP Franchise Sales Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Automate SRP franchise candidate pipeline from first contact to FDD delivery. FTC-compliant workflow.

## TRIGGER
GHL pipeline: SRP-franchise-inquiry OR Bennett says "SRP franchise pipeline".

## EXECUTION STEPS
1. Pull inquiry data from GHL
2. Send acknowledgment email (< 1 hour SLA) — standard template from Drive
3. Score candidate: liquid capital, business experience, market territory
4. Qualified (score > 6): schedule discovery call, send non-binding interest form
5. Post-discovery: if mutual interest, trigger FDD delivery workflow:
   - Log to FDD tracker (Drive: fki-legal/fdd-delivery-log.md)
   - Email FDD with 14-day review note
   - Set GHL reminder for 14-day follow-up
6. NEVER make income projections or earnings claims in any comms
7. Post pipeline update to #leo-auto daily

## COMPLIANCE RULES
- FDD must be delivered at least 14 days before any agreement signing
- All $ figures must use "financial performance representations only appear in FDD Item 19" language
- No earnings claims in any marketing, email, or call script

## DIAMOND GATE
- T1: No earnings claims. FDD-compliant language throughout ✅
- T2: File > 200 bytes ✅
- T3: FDD delivery logged, not auto-signed ✅
