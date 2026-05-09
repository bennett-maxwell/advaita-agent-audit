# SKILL-167: Franchise Renewal Manager
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Track franchise agreement expiry dates. Initiate renewal conversations 12 months in advance. Never let an agreement lapse silently.

## TRIGGER
Daily check (auto) — flag any franchise agreement expiring within 365 days.

## EXECUTION STEPS
1. Pull franchise agreement dates from Drive: `fki-franchise/agreement-tracker.md`
2. Calculate days until expiry for each franchisee
3. Milestones:
   - 365 days: send "renewal planning" email from template
   - 180 days: schedule renewal call, send updated FDD
   - 90 days: send decision deadline reminder
   - 30 days: escalate to Bennett if not renewed or non-renewed notice given
4. Log all renewal touchpoints to GHL contact
5. Upload renewal status to Drive: `fki-franchise/renewal-tracker-[date].md`
6. Post weekly renewal pipeline to #leo-auto

## COMPLIANCE
All renewals require current FDD delivery per FTC requirements.

## DIAMOND GATE
- T1: FDD compliance required at renewal ✅
- T2: File > 200 bytes ✅
- T3: Emails queued not sent — Leo review ✅
