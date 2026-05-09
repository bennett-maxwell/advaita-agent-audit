# SKILL-147: Weekly KPI Digest
**Version:** 1.0 | **Pillar:** Advanced Systems | **Reversibility:** REVERSIBLE

## PURPOSE
Every Monday: one consolidated KPI digest across all FKI brands. Bennett reads one report, knows everything.

## TRIGGER
Monday 7:30 AM MDT (auto).

## EXECUTION STEPS
1. Run in parallel:
   - Meta performance (SKILL-102 data)
   - Cash flow snapshot (SKILL-129 data)
   - P&L weekly (SKILL-137 data)
   - GHL pipeline counts (SKILL-140 data)
   - Attribution summary (SKILL-132 data)
2. Compile into ONE digest:
   - 📊 Revenue: $X (↑/↓ X% WoW)
   - 💰 Cash: $X | 30d projection: $X
   - 📱 Leads: X new | X booked | X enrolled
   - 📣 Ad Spend: $X | Blended ROAS: X.Xx
   - 🚨 Flags: [list any RED/YELLOW items]
   - ✅ Wins: [top 3 positive deltas]
3. Upload digest to Drive: `fki-reports/weekly-kpi-[date].md`
4. Post to #leo-auto (full digest)
5. Send SMS to Bennett: 5-line summary version (top metrics only)

## DIAMOND GATE
- T1: Actuals only from source APIs ✅
- T2: File > 200 bytes ✅
- T3: Report + SMS REVERSIBLE ✅
