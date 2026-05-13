# Stripe Product Configuration — for Leo to execute
**Trigger:** Leo runs this against Bennett's Stripe account
**Goal:** $47 Advaita Bootcamp checkout link, live + tested

---

## Product object
```
name: "Advaita AI Bootcamp"
description: "In 7 days, install your first AI agent — live with the founder. Three working sessions, lifetime documentation, money back if your agent isn't running by Session 2."
images: [URL to Advaita logo from FKI brand assets]
shippable: false
url: https://bennett-maxwell.github.io/fki-preview/advaita-lp.html#bootcamp
metadata:
  product_code: ADV-BOOTCAMP-47
  capacity_per_week: 5
  refund_policy: "Money-back guarantee if agent not running by end of Session 2"
  fulfillment_type: "live_sessions_plus_install"
  upsell_target: "Full Advaita engagement starting at $5,000/mo"
```

## Price object
```
unit_amount: 4700  (in cents — $47.00)
currency: usd
recurring: null  (one-time)
billing_scheme: per_unit
tax_behavior: exclusive  (apply state tax on top if applicable)
nickname: "Bootcamp — $47 one-time"
```

## Checkout Session config
```
mode: payment
ui_mode: hosted
success_url: https://bennett-maxwell.github.io/fki-preview/advaita-lp.html?bootcamp=success&session_id={CHECKOUT_SESSION_ID}
cancel_url: https://bennett-maxwell.github.io/fki-preview/advaita-lp.html#bootcamp
line_items:
  - price: <price_id from above>
    quantity: 1
customer_creation: always
customer_email: (collected on checkout)
allow_promotion_codes: false  (don't enable promo until 30+ sales validate the price)
phone_number_collection:
  enabled: true
custom_fields:
  - key: "what_business_first"
    label: { type: "custom", custom: "Your business or industry" }
    type: text
    optional: false
billing_address_collection: auto
metadata:
  campaign: "advaita-lp-bootcamp"
  funnel_position: "touch-3-post-podcast"
```

## Webhook config
```
events_to_subscribe:
  - checkout.session.completed
  - charge.refunded
  - payment_intent.payment_failed

endpoint: https://hook.us2.make.com/<MAKE_WEBHOOK_ID>
```

## Make.com scenario (wire after Stripe webhook fires)
1. **Trigger:** Stripe webhook `checkout.session.completed`
2. **Action 1:** GHL `create or update contact` with:
   - email (from Stripe customer)
   - phone (from custom field)
   - tags: `bootcamp-paid`, `funnel-stage-touch-3`, `pipeline-bootcamp`
   - custom field `business_industry` (from Stripe custom field)
   - custom field `bootcamp_purchase_date` (now)
   - custom field `bootcamp_purchase_amount` (4700 in cents)
3. **Action 2:** Calendly send invite for "Advaita Bootcamp Session 1" event type
4. **Action 3:** Gmail send via Make Gmail module — welcome email template (see `02-welcome-email.md`)
5. **Action 4:** Slack post to #leo-auto "🎉 Bootcamp purchase — {email}"
6. **Action 5:** Notion row insert in Bootcamp Pipeline DB

## Refund Webhook Path
```
trigger: charge.refunded
action_1: GHL update contact — add tag "bootcamp-refunded", remove "bootcamp-paid"
action_2: Slack post to #leo-auto "💸 Bootcamp refund — {email} — reason?"
action_3: Notion row update Bootcamp Pipeline DB — status "Refunded"
```

## Testing checklist before Leo flips live
- [ ] Stripe product created
- [ ] Price ID exists
- [ ] Checkout link works (test card 4242 4242 4242 4242)
- [ ] Webhook fires Make.com on test purchase
- [ ] GHL contact created with all 4 tags
- [ ] Calendly invite arrives in test inbox
- [ ] Welcome email arrives in test inbox
- [ ] Slack post in #leo-auto on test purchase
- [ ] Notion row inserted
- [ ] Refund flow tested (refund the test charge, verify all cleanup)

## Final live checkout link format (Leo replaces in landing page after wire)
```
https://buy.stripe.com/<short_link_id>
```
That URL replaces `STRIPE_CHECKOUT_URL_PENDING` in `01-sales-section.html`.

## Bennett-gate touchpoints
- Stripe account ownership — Bennett (account already exists, no new account needed)
- Domain verification on Stripe (franchiseki.com or bennett-maxwell.github.io) — Bennett one-click
- Tax registration if state collects on digital services — Bennett confirms (US Central tax law)

## Definition of done
Live checkout URL pasted into a Slack receipt to #leo-auto + tested with a real $1 micro-purchase by Bennett himself (refunded immediately for cleanup) + screenshot of the success page captured + GHL contact verified created with all tags.
