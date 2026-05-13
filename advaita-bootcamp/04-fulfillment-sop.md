# Bootcamp Fulfillment SOP — what Bennett/installer actually does
**Use:** Every Bootcamp purchase. Print this. Stick to it.

---

## Session 1 (60 min) — Discovery + Agent Selection
**When:** Booked via Calendly within 2 days of purchase
**Pre-work (Bennett, 15 min before call):**
- Read buyer's blueprint quiz output (from GHL contact custom fields)
- Read buyer's NotebookLM podcast transcript (Drive link in GHL)
- Pre-list 2–3 candidate agents with rough ROI for their stack

**On the call (60 min):**
1. 5 min — Re-confirm: their stack, their top time-drain, their decision criteria
2. 10 min — Walk through 2–3 candidate agents, ROI per agent
3. 5 min — Pick the ONE we install
4. 30 min — Get read access to their tools. Confirm exact data inputs the agent will need.
5. 10 min — Confirm Session 2 date (48–72 hrs out)

**Deliverable end of call:**
- One-page "Agent Spec" doc shared with buyer (what we're building, what data it touches, what guardrails it has)
- Calendar invite for Session 2

---

## Between Sessions (48 hours) — Build
**Owner:** Senior installer (or Bennett if no installer available)
**Work:**
1. Build the agent in our framework
2. Test against sample data from buyer's tools
3. Document: setup, inputs, outputs, escalation rules, kill switch
4. Stage in buyer's environment but DO NOT activate (they activate live in Session 2)

**Definition of ready for Session 2:**
- Agent runs end-to-end against test data with 95%+ accuracy
- Documentation file written
- One pre-recorded 2-min "this is what it does" video for the buyer to watch BEFORE Session 2

**If build runs over 48 hours:** email buyer, push Session 2 to next available slot, no refund triggered. If pattern repeats (>1 over-run per 5 builds), audit the agent-selection criteria — we're picking too-complex agents in Session 1.

---

## Session 2 (45 min) — Deploy + Train
**Pre-work:** confirm buyer watched the 2-min video. If not, walk through it first 5 min.

**On the call (45 min):**
1. 10 min — Final review: any changes needed before going live
2. 10 min — Deploy. Agent activates in their environment. Watch the first real input.
3. 15 min — Train the buyer: how to read the agent's log, how to pause it, how to escalate
4. 5 min — Hand over documentation
5. 5 min — Set Session 3 (D+7) on calendar

**Deliverable end of call:**
- Agent running in production
- Buyer trained on monitor/pause/escalate
- Session 3 booked

**Refund trigger:** if the agent is NOT running in production by end of Session 2 (technical failure or scope mismatch), Bennett refunds the $47 same-day and buyer keeps the documentation.

---

## D+0 to D+7 — Async observation period
**Buyer-side:**
- Watches the agent run
- Logs daily hours saved
- Emails Bennett if anything breaks

**Bennett-side:**
- Reads any escalation emails from the buyer within 4 business hours
- If agent breaks in a way the buyer can't self-fix, jump in async (slack-style, not a new call)

---

## Session 3 (30 min) — Retrospective
**Pre-work:** review the agent's 7-day run log

**On the call (30 min):**
1. 10 min — Recap: what worked, what didn't, hours saved estimate
2. 10 min — Three options walkthrough (keep / DIY add / full Advaita engagement)
3. 10 min — Whatever they pick, set the follow-up

**Deliverable end of call:**
- Recap email (D+7 email template)
- If they pick "full engagement," scoping call booked separately
- If they pick "keep" or "DIY," they're released. We follow up in 30 days for a check-in.

---

## Refund SOP
**Trigger:** buyer requests OR agent isn't running by end of Session 2 OR our build runs >7 days
**Action:**
1. Bennett confirms in Slack (no auto-refund — needs human eyes on each)
2. Stripe refund initiated same-day
3. Refund email sent (see onboarding template #4 — refund version)
4. GHL contact tagged `bootcamp-refunded`
5. Documentation stays with the buyer permanently
6. Log refund reason in Notion `bootcamp-refund-log` for monthly review

**Refund rate target:** ≤10%. If it exceeds 10% in a month, audit Session 1 agent-selection accuracy.

---

## Capacity Lock
- 5 Bootcamps/week MAX (across Bennett + 1 senior installer)
- Calendly limits Session 1 slots to 5/week — when full, auto-waitlist
- If pipeline hits 7+ purchases/week 3 weeks running, hire a 2nd installer OR raise price to $97 to throttle

---

## Hand-off note
This SOP is Diamond-verified T1/T2/T3 as of 2026-05-13. Update via PATCH on the Drive copy. Do not edit in place during a live Bootcamp run.
