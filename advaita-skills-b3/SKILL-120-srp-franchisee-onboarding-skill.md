# SKILL-120: SRP Franchisee Onboarding Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Automate SRP franchisee onboarding from signed agreement through grand opening readiness. 90-day playbook executed without manual management.

## TRIGGER
GHL stage: SRP-franchise-signed.

## EXECUTION STEPS
1. Create franchisee Notion page from template (90-day onboarding tracker)
2. Trigger Day 0 welcome sequence:
   - Welcome email with portal access
   - Training schedule link
   - Dedicated Slack channel creation
3. Schedule milestone check-ins at Day 7, 30, 60, 90
4. Week 2: training completion check — if < 80% complete, alert Leo
5. Week 4: location lease confirmation check
6. Week 8: inventory order confirmation check
7. Grand opening: trigger press release template + local marketing package
8. Log all milestones to Drive: `fki-franchise/onboarding/[franchisee-id].md`
9. Post weekly status to #leo-auto

## DIAMOND GATE
- T1: No revenue projections in onboarding materials ✅
- T2: File > 200 bytes ✅
- T3: Milestone checks REVERSIBLE. No spend auto-committed ✅
