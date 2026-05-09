# SKILL-146: Anomaly Detection System
**Version:** 1.0 | **Pillar:** Advanced Systems | **Reversibility:** REVERSIBLE

## PURPOSE
Detect statistical anomalies across FKI metrics. Revenue spikes/drops, ad spend outliers, lead volume changes. Alert before problems become crises.

## TRIGGER
Daily 6 AM MDT (auto).

## EXECUTION STEPS
1. Pull last 30d daily metrics from QB + Meta Ads API + GHL:
   - Daily revenue
   - Daily ad spend
   - Daily leads
   - Daily enrollments
2. Calculate rolling 7d averages and standard deviations
3. Flag: any metric deviating > 2 standard deviations from 7d average
4. Classify severity:
   - 2-3 SD: YELLOW (investigate)
   - > 3 SD: RED (immediate alert)
5. For RED: immediately post to #leo-auto with metric, expected value, actual value, % deviation
6. Log anomaly log to Drive: `fki-monitoring/anomaly-log-[date].md`
7. Weekly anomaly summary to #leo-auto

## DIAMOND GATE
- T1: Statistical methodology disclosed. No predictive claims ✅
- T2: File > 200 bytes ✅
- T3: Alert only — no auto-remediation ✅
