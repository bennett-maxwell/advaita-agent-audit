# Advaita AI Bootcamp — $47 · Product Master Spec
**Created:** 2026-05-13 (Hyperagent / bennett-mode-skill v2.1)
**Owner:** Bennett Maxwell · FranchiseKI / Advaita-for-Business
**Status:** SPEC LOCKED — ready for Stripe wire-up

---

## The One-Line Pitch
"In 7 days, install your first AI agent — guided live by the founder. $47, money-back if your install doesn't work."

## What This Is (and isn't)
**Is:** A 7-day guided micro-engagement. Buyer fills the Advaita intake quiz, gets the free blueprint + custom NotebookLM podcast, then upgrades for $47 to get a live install of their FIRST AI agent in their actual stack — done WITH them by Bennett or a senior Advaita installer over 3 working sessions across one calendar week.

**Is not:**
- Not a course. No videos to consume passively.
- Not a "framework download." It's an actual install.
- Not the full Advaita engagement. That's a separate quote starting after the Bootcamp.
- Not a SaaS subscription. One-time fee.

## Price Logic
**$47** is intentional:
- Below $50 = below most prospects' "ask the spouse" threshold → faster yes
- Above $39 = filters tire-kickers, attracts serious operators
- Below $99 = removes the price objection from blueprint-to-purchase
- $47 covers ~30 min of senior install time × 3 sessions = the actual marginal cost is ~breakeven; the product is positioned as **lead generator for the full Advaita engagement**, not a profit center
- Easy mental math: 100 Bootcamp sales = $4,700 → covers a senior installer for ~2 weeks

## What the Buyer Gets (deliverable list)
1. **60-min Session 1 — Discovery + agent selection.** Live with Bennett or a senior Advaita installer. Audit-blueprint reviewed; ONE agent selected for install (the highest-ROI one based on their stack).
2. **48 hr async — agent built.** Installer builds the agent, deploys to their environment (their CRM/email/whatever), tests with sample data.
3. **45-min Session 2 — Deploy + train.** Live working session. Agent goes live in their actual environment. Buyer is trained on how to monitor + adjust.
4. **30-min Session 3 — D+7 retrospective.** One week later. Did it work? What broke? Buyer keeps the agent and the documentation.
5. **Lifetime access** to the install documentation (markdown file in their Drive/email).
6. **Refund guarantee:** if the agent isn't running by end of Session 2, full $47 refund + the agent doc stays with the buyer.

## What Bennett's Side Has to Build (Bennett Mode)
- Stripe product + checkout link
- Welcome email auto-trigger on purchase
- Calendly link for Session 1 (15-min slots, M-F, business hours US Central)
- Onboarding email sequence (D+0 welcome / D+1 reminder / D+3 mid-check / D+7 retro)
- Fulfillment SOP (3 sessions, what gets done in each)
- Refund SOP

## Capacity Math (truth gate)
At 1 founder + 1 senior installer:
- ~5 Bootcamps/week capacity (each is 2.25 hrs of live time)
- 20/month max
- Pipeline gate: when Bootcamp purchases hit 4/week, route the 5th onward to a waitlist OR price step to $97 to throttle

## Funnel Position (per Option C from earlier approval)
Touch-1 outreach → **NO** Bootcamp mention (free blueprint only)
Touch-2 follow-up (post-blueprint) → **NO** Bootcamp mention (free podcast delivery)
Touch-3 follow-up (post-podcast, ~D+7-14 of nurture) → **First** Bootcamp mention
Touch-4 (D+21) → Reminder/scarcity

Reason: Option C honored. Bootcamp is the natural conversion AFTER value-delivery, not cold-pitched.

## Success Metrics (T+30 day check)
- ≥10 Bootcamp purchases attributed to outreach this run
- ≥80% of Session 1s actually held
- ≥70% of installs live by end of Session 2
- ≥1 Bootcamp buyer upgrades to full Advaita engagement at $5K+

## Refund Math (no-spin policy)
If 1 in 10 buyers refunds, total refund cost = $47 × 1 = $47.
Margin per non-refund = ~zero (intentionally — this is lead gen, not revenue).
Margin from upgrades is where this product makes money. One $5K upgrade pays for 100 Bootcamps including refunds.

## Compliance Notes
- $47 is not an "earnings claim" — no FDD qualifier required on price
- Bootcamp is NOT a franchise sale, NOT a financial advisory service — just AI installation work-for-hire
- Refund language is real and binding (no fine print games)
- Bootcamp pricing is value-first; do not anchor against $99 or $499 ("$47 from $499!") because there is no $499 list price — that would be deceptive

## Open Items (auto-dispatched to Leo this run)
- Create Stripe product + $47 checkout link (Composio Stripe action or direct API)
- Wire Stripe webhook → GHL contact create + tag "bootcamp-paid"
- Create Calendly event type "Advaita Bootcamp Session 1" (15-min discovery slots)
- Wire Make.com scenario: Stripe webhook → Calendly email auto-send
- Add Bootcamp section to advaita-lp.html (HTML attached separately)

## Sign-off
Created via bennett-mode-skill v2.1 chain (compressed for product-build scope). Diamond verified T1/T2/T3.
