# SKILL-102: Meta Ad Performance Monitor
**Version:** 1.0 | **Pillar:** Marketing Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Daily automated pull of Meta ad performance across all FKI brands. Flags underperformers. Surfaces wins. No human data-pulling required.

## TRIGGER
Daily at 7:00 AM MDT (auto). OR Bennett says "meta report".

## EXECUTION STEPS
1. Pull last 24h data from Meta Ads API for all brand ad accounts:
   - IC ad account ID (from Drive: fki-config/ad-account-ids.md)
   - SH ad account ID
   - SRP ad account ID
2. For each active ad set, compute:
   - ROAS = Revenue / Spend
   - CPL = Spend / Leads
   - CTR
   - Frequency
3. FLAG conditions:
   - ROAS < 1.0x AND active > 24h → "STRIKE PROTOCOL" alert
   - Frequency > 4.0 → "FATIGUE" alert
   - CTR < 0.8% → "CREATIVE SWAP" alert
4. Format delta-only report (only changed/flagged items vs yesterday)
5. Post to #leo-auto with flags + raw numbers
6. Log to Drive: `fki-reports/meta-daily-[date].md`

## OUTPUT
Delta performance table. Flag list. Leo work orders if any flags triggered.

## DIAMOND GATE
- T1: Report raw API numbers only — no projections or income claims ✅
- T2: File > 200 bytes ✅
- T3: Read-only + Slack post REVERSIBLE ✅
