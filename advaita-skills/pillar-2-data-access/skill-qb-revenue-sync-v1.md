---
skill: quickbooks-revenue-sync
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI pulls QB revenue data automatically — replaces manual financial reporting
---
# QuickBooks Revenue Sync Skill v1

## Purpose
Automated daily revenue data pull from QuickBooks. AI generates financial summary posted to #leo-auto. Bennett never has to open QB to know where the business stands.

## Sync Schedule
- 8:00 AM MDT: Daily revenue summary
- 12:00 PM MDT: Mid-day refresh (pipeline vs. actual)
- 5:00 PM MDT: End-of-day close

## Data Points Pulled (REVERSIBLE — read-only QB access)
- Today's revenue (vs. same day last week, same day last month)
- MTD revenue (vs. MTD goal, vs. prior month same date)
- YTD revenue (vs. YTD goal)
- Open invoices / accounts receivable
- Recent transactions (last 24h)

## Data Source Verification
All figures pulled directly from QB. Never reported without QB API confirmation. If QB API fails: note in report "Source unavailable — figures from last successful sync [timestamp]."

## Daily Revenue Report Format (Slack → #leo-auto)
```
📊 FKI DAILY REVENUE — [Date] [Time] MDT
Today: $X (QB-verified) | vs. LW: +/-X%
MTD: $X | Goal: $X | Gap: $X
YTD: $X | On track: YES/NO
Pipeline (estimated close this month): $X
```
Note: All figures from QuickBooks API; consult your accountant for financial decisions.

## Error Handling
QB API unavailable → post to #leo-auto: "QB sync failed [timestamp]. Last data: [prior sync]. Ivan-CC to investigate if persists >2h."

## Autonomy Value
**Replaces:** Bennett or CFO manually opening QB to check revenue.
**Result:** Revenue visibility delivered automatically, 3x daily. Bennett always knows the number.
**Advaita gap closed:** Financial reporting automation — from 0% → 100% AI-autonomous.
