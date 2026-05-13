# Onboarding Email Sequence — Day 0 / 1 / 3 / 7
**Trigger chain:** Stripe webhook → GHL workflow → 4-step drip
**From:** bennett@franchiseki.com

---

## Email 1 — D+0 (Welcome, immediate)
See `02-welcome-email.md`. Sent within 60 seconds of Stripe success.

---

## Email 2 — D+1 (Calendly reminder if not booked)
**Trigger condition:** if {{calendly_booked}} == false at D+1 08:00 local
**Subject:** Quick — book your Bootcamp Session 1 today

Hi {{first_name}},

Yesterday you bought the Advaita Bootcamp. I haven't seen your Session 1 booking yet — that's the part where you and I get on the phone and pick which agent to install.

**Book here (3-second click):** {{calendly_link}}

If something's preventing you from scheduling, just reply to this email and tell me. We can do it async via email if calendar is the blocker. The clock on your 7-day install starts at Session 1, so let's get it on the books.

— Bennett

---

## Email 3 — D+3 (mid-check / post-Session-2)
**Trigger condition:** sent ~24 hours after Session 2 confirmation
**Subject:** {{first_name}} — your agent is live. Now the boring part.

Hi {{first_name}},

Your agent went live in Session 2 yesterday. Three things matter in the next 5 days:

**1. Watch it run.**
Don't change anything yet. Just observe. The agent's job in week one is to prove it does what we said it does. If you see something weird, screenshot it and reply to this email. Don't disable it without telling me.

**2. Log the "saved" hours.**
At the end of each day, write down: how many hours of admin work did this agent do that I would have done myself? Even rough numbers. We'll review the total at Session 3.

**3. Don't add to it yet.**
The temptation after one working agent is to immediately stack 3 more. Wait. One agent running clean is worth more than 4 agents running half-broken.

**Session 3 (D+7 from your purchase) is the retrospective.** That's when we decide together if you want to extend the Bootcamp into a full Advaita engagement (separate, custom-quoted) or just keep the one agent and call it complete.

— Bennett

---

## Email 4 — D+7 (Session 3 retrospective + upsell offer)
**Trigger:** immediately after Session 3 ends (manual fire by Bennett, or auto via Calendly hook)
**Subject:** {{first_name}} — your retrospective, and what's next

Hi {{first_name}},

Great Session 3. Here's the recap of where we landed:

- Agent installed: {{agent_name}}
- Hours/week saved (your estimate): {{hours_saved}}
- ROI on the $47: {{roi_multiplier}}× (if {{hours_saved}} × $50/hr is the math)

**Three things you can do from here:**

**Option 1 — Keep the agent, that's it.**
You're done. The Bootcamp delivered what it promised. The agent runs forever. You have the documentation. You're free to disappear and just collect the time savings.

**Option 2 — Add another agent yourself.**
We taught you the install pattern in Session 2. You have the documentation. If you want to add a 2nd agent on your own, the docs walk you through it. We're a reply away if you get stuck.

**Option 3 — Run the full Advaita engagement.**
You saw what one agent does. The full Advaita stack is 7–12 agents working together with shared memory, escalation paths, and a unified ops dashboard. Engagement starts at $5,000/mo, quoted custom based on your stack. Reply "Advaita" and I'll send the proposal.

**Whatever you pick, your $47 was honored.** That was the deal.

— Bennett

---

## Refund email (manual fire if buyer requests)
**Subject:** Refund processed — agent docs stay with you

Hi {{first_name}},

Your $47 has been refunded to your card. Should hit in 3–5 business days depending on bank.

The agent documentation we built stays with you — that's the deal we made on the landing page. If you ever want to come back and try a different agent, send me a note. No hard feelings either way.

— Bennett
