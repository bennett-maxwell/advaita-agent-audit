# SKILL-111: IC Coaching Enrollment Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Automate Illegal Civilizations coaching enrollment workflow from booked call to payment to onboarding. Reduces Bennett's back-office time to zero.

## TRIGGER
GHL pipeline stage moves to "Booked" for IC coaching offer.

## EXECUTION STEPS
1. Pull contact data from GHL (name, email, phone, survey responses)
2. Generate personalized pre-call prep email using IC brand voice
3. After call: check GHL for "Won" stage update
4. On "Won":
   - Send payment link (Stripe or ThriveCart — from Drive: fki-config/payment-links.md)
   - Create onboarding Notion page from template
   - Add to IC Coaches Slack channel
   - Schedule Day 1 kickoff call in Google Calendar
   - Tag GHL: ic-enrolled, cohort-[current cohort ID]
5. Send welcome email + onboarding packet link
6. Log enrollment to QB as new revenue entry (REVERSIBLE — QB draft, not posted)
7. Post receipt to #leo-auto: name, offer, $ amount, cohort

## DIAMOND GATE
- T1: No income projections in any enrollment comms ✅
- T2: File > 200 bytes ✅
- T3: QB entry is draft (not posted). All else REVERSIBLE ✅
