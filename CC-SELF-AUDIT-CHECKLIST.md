# CC Self-Audit Checklist (command-center-skill § Self-Audit)

## Run this checklist weekly (Angie mini-audit Tue/Fri 9AM MDT)

1. [ ] All 8 CC pages return HTTP 200 (dashboard.franchiseki.com/*)
2. [ ] hub/index.html KPI strip: YTD revenue, autonomy %, CPL all current (<7d)
3. [ ] cc-data-snapshot.json exists and snapshot_date < 24h
4. [ ] Human gates count badge matches actual open gates
5. [ ] Legal deadline banner shows correct days-until (update daily)
6. [ ] Marketing CPL and spend match latest Meta snapshot
7. [ ] Personal Finance / Finny shows Kay OAuth gate status
8. [ ] Real Estate / Rachel shows properties count (>=4 expected)
9. [ ] Autonomy % in hub matches advaita-autonomy-baseline.json (+-0.5%)
10. [ ] All CC card links resolve correctly (no 404s)
11. [ ] machine-health.json updated within 24h
12. [ ] No "demo_mode: true" in any data JSON
13. [ ] Legal CC password protection active (franchiseki2024)
14. [ ] Finance CC password protection active (franchiseki2024)
15. [ ] git log shows push within 24h (data freshness gate)

## Auto-fix triggers (Angie)
- Item 1 fail: DM Bennett + post #leo-coaches
- Items 2-4 fail: re-run cc-daily-refresh.sh cron
- Item 5 fail: update legal alert text + commit + push
- Item 12 fail: flip demo_mode false + commit + push
- Item 15 fail: re-run refresh cron on Ivan
