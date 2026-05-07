---
skill: google-analytics-traffic-monitor
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI monitors FKI website traffic — replaces manual GA dashboard checking
---
# Google Analytics Traffic Monitor Skill v1

## Purpose
Weekly automated pull of FKI website traffic data. AI surfaces SEO performance, content winners, and lead conversion data from organic traffic.

## Monitored Metrics (REVERSIBLE — read-only GA4 access)

**Traffic Volume**
- Weekly sessions (vs. prior week, vs. prior year)
- Organic search sessions (primary SEO health metric)
- Top landing pages by session volume
- New vs. returning visitor ratio

**SEO Performance**
- Top organic search terms driving traffic
- Pages ranking for target keywords (franchise consultant, franchise broker, MapKi, FranchiseKI)
- Organic click-through rate trend

**Conversion Metrics**
- Sessions → Lead Form submissions (conversion rate)
- Top pages that drive form conversions
- Drop-off pages (high traffic, low conversions → content improvement opportunity)

## Weekly Traffic Report (every Monday, #leo-auto)
```
📈 FKI TRAFFIC WEEK OF [date]
Sessions: X (vs. LW: +/-X%)
Organic: X% of total
Top page: [page] — X sessions
Lead conversions: X (X% conversion rate)
Top SEO opportunity: [keyword/page identified]
```

## AI Keyword Omnipresence Tracking
Special tracking for Advaita SEO goal — FKI citation rate in AI search responses:
Currently: 1/5 AI keywords citing FKI. Target: 3/5 by June 5, 2026.
Weekly check: Monitor for FKI mentions in AI-generated franchise content.

## Autonomy Value
**Replaces:** Manual Google Analytics dashboard review.
**Result:** Traffic insights delivered automatically. Content and SEO strategy decisions are data-driven.
**Advaita gap closed:** Web analytics monitoring — from 0% → 100% AI-autonomous.
