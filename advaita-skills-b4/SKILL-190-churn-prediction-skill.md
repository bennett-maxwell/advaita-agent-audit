# SKILL-190: Churn Prediction Engine
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Predict which FKI coaching clients are at risk of churning before they actually churn. Enable proactive retention.

## TRIGGER
Weekly Tuesday 7 AM MDT (auto).

## EXECUTION STEPS
1. Pull all enrolled clients from GHL (IC + SH)
2. Score each client on 10 churn indicators:
   - Days since last login (0-2: low, 3-7: medium, 8-14: high, 14+: critical)
   - Assignment completion rate (<50%: flag)
   - Call attendance rate (<60%: flag)
   - NPS score at last survey (<7: flag)
   - Response time to coach emails (>48h: flag)
   - Support tickets opened this month (>2: flag)
   - Payment delays (any: flag)
   - Social media engagement with brand (none in 14d: flag)
   - Milestone progress vs cohort (bottom quartile: flag)
   - Upsell interest expressed (zero: neutral)
3. Composite churn risk score (0-100)
4. HIGH risk (>70): immediate intervention — draft personal email from Bennett
5. MEDIUM risk (40-70): trigger re-engagement sequence
6. LOW risk (<40): standard nurture
7. Log predictions to Drive: `fki-intelligence/churn-predictions-[date].md`
8. Post HIGH risk count to #leo-auto

## DIAMOND GATE
- T1: Predictions labeled as risk indicators, not certainties ✅
- T2: File > 200 bytes ✅
- T3: Intervention emails queued — Leo activates ✅
