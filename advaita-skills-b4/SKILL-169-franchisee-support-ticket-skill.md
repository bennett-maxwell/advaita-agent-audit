# SKILL-169: Franchisee Support Ticket System
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Automate SRP franchisee support requests. Triage, route, and resolve common issues without franchisee support staff.

## TRIGGER
Inbound email to SRP support address OR GHL form submission.

## EXECUTION STEPS
1. Parse support request: category + urgency + franchisee ID
2. Auto-triage categories:
   - Operational: match to SRP ops manual answer (SKILL-157 data)
   - Technology: route to Leo CLI
   - Legal/compliance: queue for Bennett review (> 24h SLA)
   - Vendor: route to vendor management workflow (SKILL-159)
   - Training: route to training tracker (SKILL-158)
3. For auto-resolved tickets: send answer + close
4. For escalated: create GHL task + notify Leo in #leo-auto
5. Track: ticket volume, resolution time, category breakdown
6. Log to Drive: `fki-franchise/support-tickets-[month].md`
7. Post weekly support stats to #leo-auto

## DIAMOND GATE
- T1: No guidance that constitutes legal advice ✅
- T2: File > 200 bytes ✅
- T3: Auto-resolution REVERSIBLE. Legal tickets require Bennett ✅
