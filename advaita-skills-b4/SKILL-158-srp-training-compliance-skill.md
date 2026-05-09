# SKILL-158: SRP Training Compliance Monitor
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Ensure all SRP franchisees complete required initial training and ongoing education. FDD compliance tracking.

## TRIGGER
Weekly Thursday 8 AM MDT (auto).

## EXECUTION STEPS
1. Pull SRP franchisee roster from Drive: `fki-franchise/franchisee-roster.md`
2. Pull training completion records from Notion or Drive tracker
3. Check required training per FDD:
   - Initial training: must complete before opening
   - Annual refresher: within 365 days of last completion
   - Product training: when new SKU launches
4. Flag:
   - Franchisees past opening without completed initial training → RED alert
   - Annual refresher overdue > 30d → YELLOW alert
5. For flags: draft compliance notice from Drive template
6. Post to #leo-auto: compliance status by franchisee
7. Log compliance report to Drive: `fki-franchise/training-compliance-[date].md`

## DIAMOND GATE
- T1: Compliance tracking only — no performance claims ✅
- T2: File > 200 bytes ✅
- T3: Notices drafted not sent — Leo review ✅
