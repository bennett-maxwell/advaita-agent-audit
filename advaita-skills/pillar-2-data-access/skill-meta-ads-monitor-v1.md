---
skill: meta-ads-performance-monitor
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI monitors Meta Ads spend/performance daily — replaces manual ad account checking
---
# Meta Ads Performance Monitor Skill v1

## Purpose
Daily automated pull of Meta Ads performance data. AI flags anomalies and surfaces optimization opportunities before they become expensive problems.

## Monitored Metrics (REVERSIBLE — read-only API access)
- Daily spend (vs. budget, vs. prior day, vs. 7-day average)
- Cost per lead (vs. target; target defined in campaign settings)
- Lead volume (vs. daily target)
- Click-through rate (vs. campaign benchmark)
- Cost per click (trend vs. prior week)
- Top-performing ad (highest volume, lowest CPL)
- Underperforming ad (highest spend, lowest leads)

## Alert Thresholds (auto-post to #leo-auto)

**SPEND ALERT**: Daily spend >120% of daily budget target → immediate alert (IRREVERSIBLE: spending — flag only, do NOT change budget without Bennett approval)

**CPL ALERT**: Cost per lead >150% of target for 3+ consecutive days → alert + hypothesis on cause

**VOLUME DROP**: Lead volume <50% of daily target for 2+ consecutive days → alert + creative/targeting review recommendation

**CREATIVE FATIGUE**: Any ad running >21 days with declining CTR trend → refresh recommendation

## Weekly Ad Report (every Monday, #leo-auto)
- Week spend vs. budget
- Lead volume and CPL trend
- Top 3 performing ads
- Recommended test for coming week (creative, audience, or bid strategy)

## IRREVERSIBLE Gate
Any change to budget, bid strategy, audience, or ad creative = IRREVERSIBLE → daily digest only, never auto-executed.

## Autonomy Value
**Replaces:** Manually logging into Meta Ads Manager to check performance.
**Result:** Ad problems caught within 24h, not weeks. Spend efficiency maintained automatically.
**Advaita gap closed:** Paid media monitoring — from 0% → 100% AI-autonomous (monitoring); budget changes require Bennett sign-off.
