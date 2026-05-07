---
skill: lead-source-attribution
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI tracks lead source from first touch to close — replaces guessing what marketing is working
---
# Lead Source Attribution Skill v1

## Purpose
Track every lead from source to close (or drop). AI produces weekly attribution reports that show exactly which marketing channels and content pieces are driving revenue.

## Attribution Data Points (read from GHL)
- `contact.source` field (set at intake)
- UTM parameters from form submission (meta paid, organic, referral, direct)
- Landing page at time of form submit
- Content piece that drove conversion (specific article, guide, or ad)

## Attribution Categories
- Meta Paid (campaign, ad set, ad)
- Organic SEO (landing page, keyword)
- Referral (source referral partner or franchisee)
- Direct (typed URL, saved bookmark)
- Email (FKI newsletter or sequence re-engagement)
- Partner (co-marketing, FDD referral)

## Attribution → Revenue Mapping
When deal closes: AI maps backward through attribution chain.
Output: "This close attributed to [source] → [landing page] → [sequence touchpoint]."

## Weekly Attribution Report (#leo-auto)
- Leads this week by source
- Lead quality by source (average FranchiseScore per source)
- Closes in last 30 days by source
- Cost per lead by source (Meta paid CPL vs. organic CPL)
- ROI by channel: closes per channel / cost per channel (Meta) or cost per content piece (SEO)

## Marketing Investment Decision Support
Data feeds directly to: Meta Ads optimization (skill-meta-ads-monitor-v1), SEO content strategy (skill-google-analytics-traffic-v1), and referral program (skill-referral-program-intelligence-v1).

## Autonomy Value
**Replaces:** Guessing which marketing is working.
**Result:** Every marketing dollar allocation decision is backed by actual close data. FKI continuously optimizes.
**Advaita gap closed:** Marketing attribution intelligence — from 0% → 90% AI-autonomous.
