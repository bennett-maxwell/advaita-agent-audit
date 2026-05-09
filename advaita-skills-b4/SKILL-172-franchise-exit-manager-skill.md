# SKILL-172: Franchise Exit Manager
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Manage SRP franchisee exits: voluntary non-renewal, termination, transfer, or buyback. FTC-compliant process.

## TRIGGER
Bennett says "franchise exit [franchisee]" OR franchisee submits non-renewal notice.

## EXECUTION STEPS
1. Determine exit type: non-renewal / termination / transfer / buyback
2. Load exit checklist from Drive: `fki-franchise/exit-checklist.md`
3. Log exit notice date (critical for FTC notice period compliance)
4. Generate exit tasks:
   - Debranding timeline (signage, marketing materials)
   - Inventory disposition
   - Technology access termination
   - Final royalty reconciliation
5. For transfers: generate buyer approval checklist (FDD delivery required)
6. ALL STEPS require Bennett legal gate before execution
7. Upload exit plan to Drive: `fki-franchise/exits/[franchisee-id]-exit-[date].md`
8. Post to #leo-auto: exit type + timeline summary

## COMPLIANCE
Franchise terminations carry significant legal obligations. Every step requires legal counsel review.

## DIAMOND GATE
- T1: Legal gate mandatory on all execution steps ✅
- T2: File > 200 bytes ✅
- T3: Plan only — Bennett legal gate before any action ✅
