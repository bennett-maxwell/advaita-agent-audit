---
skill: pipeline-value-report
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI generates pipeline value report — Bennett always knows forward revenue without asking
---
# Pipeline Value Report Skill v1

## Purpose
Daily automated calculation of FKI's pipeline value — probability-weighted forecast of commissions in the pipeline. Bennett always knows the revenue outlook.

## Pipeline Value Calculation

For each active candidate in GHL:
1. Identify current stage
2. Apply stage close probability:
   - New Lead: 5%
   - Discovery Completed: 20%
   - FDD Review: 35%
   - Validation: 55%
   - Pending Award: 80%
   - Awarded: 100%
3. Multiply by estimated commission value (per brand being discussed; rates vary by franchisor)
4. Sum all probability-weighted values = Pipeline Value

Note: All pipeline values are estimates based on stage probability and estimated commission rates. Actual commissions confirmed upon franchisor payment. Not a financial guarantee. Consult your accountant for financial planning.

## Daily Pipeline Report (#leo-auto, 8 AM MDT)
```
📊 FKI PIPELINE — [Date]
Active Candidates: X
Hot (score 80+): X
Total Probability-Weighted Pipeline: $X (estimated; see above)
Expected Closes This Month: X
Expected Closes Next Month: X
```

## Weekly Pipeline Trend
Monday report includes: pipeline value vs. prior week, candidate count by stage, close rate trend (30-day rolling).

## Autonomy Value
**Replaces:** Bennett asking brokers "where's our pipeline?"
**Result:** Pipeline value delivered automatically every morning. Forward-looking revenue visibility without any human input.
**Advaita gap closed:** Revenue forecasting — from 0% → 90% AI-autonomous.
