# SKILL-101: Meta Campaign Launch Automation
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Launch new Meta ad campaigns for FKI brands without human input. Pulls creative from approved library, sets targeting from ICP profiles, submits for review.

## TRIGGER
Bennett says "launch [brand] Meta campaign for [offer]" OR weekly autopilot detects budget available + no active campaign for offer.

## INPUTS
- Brand: IC | SH | SRP
- Offer name
- Budget (default: $50/day per ad set)
- Creative brief OR creative ID from approved library

## EXECUTION STEPS
1. Load brand ICP from Drive: `fki-icp-profiles/[brand]-icp.md`
2. Pull last 3 winning ad creatives from Meta Ads API (ROAS > 1.5x, last 30d)
3. Generate 3 ad copy variants using bennett-intelligence-layer-skill
4. Create campaign via Meta Marketing API:
   - Objective: CONVERSIONS
   - Pixel: brand-specific pixel ID
   - Targeting: ICP age/geo/interest stack
   - Budget: daily cap from input
5. Submit creatives for review
6. Log campaign ID + ad set IDs to GHL contact note
7. Post receipt to #leo-auto: campaign name, budget, targeting summary, campaign ID

## OUTPUT
- Meta campaign ID
- 3 ad set IDs
- Estimated daily reach
- Slack receipt in #leo-auto

## DIAMOND GATE
- T1: No $ claims without "results may vary" qualifier. No income guarantees.
- T2: File size > 200 bytes ✅
- T3: Campaign creation REVERSIBLE (can pause/delete). No spend committed until human approves review. ✅

## REVERSIBILITY: REVERSIBLE
Campaign created in PAUSED state. No spend until Bennett approves activation.
