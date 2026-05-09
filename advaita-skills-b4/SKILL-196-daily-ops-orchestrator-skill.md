# SKILL-196: Daily Ops Orchestrator
**Version:** 1.0 | **Pillar:** Autonomy Glue | **Reversibility:** REVERSIBLE

## PURPOSE
The master daily automation sequence. Runs all daily monitoring skills in the correct order. Bennett wakes up to a fully briefed world.

## TRIGGER
Daily 6:00 AM MDT (auto).

## EXECUTION SEQUENCE (in order)
1. SKILL-193: Data Quality Monitor
2. SKILL-150: System Health Dashboard
3. SKILL-144: GHL Automation Health Monitor
4. SKILL-102: Meta Ad Performance Monitor
5. SKILL-103: Google Ads Performance
6. SKILL-129: Cash Flow Monitor
7. SKILL-133: CPA Target Monitor
8. SKILL-135: Budget Pacing Monitor
9. SKILL-146: Anomaly Detection
10. SKILL-123: Brand Reputation Monitor
11. SKILL-187: Decision Log (any overnight decisions)
12. SKILL-124: Coaching Call Prep (if calls today)

## OUTPUT
- Individual skill receipts in #leo-auto
- Daily master summary post by 6:30 AM MDT:
  "🌅 FKI DAILY BRIEF — [date]
  Systems: [health status]
  Cash: $X | ROAS: X.Xx | Leads: X
  Flags: [count] — [top flag]
  Today's calls: [count]"

## DIAMOND GATE
- T1: Aggregate of compliant skills ✅
- T2: File > 200 bytes ✅
- T3: All constituent skills REVERSIBLE ✅
