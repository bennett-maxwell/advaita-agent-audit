# SKILL-150: System Health Dashboard
**Version:** 1.0 | **Pillar:** Advanced Systems | **Reversibility:** REVERSIBLE

## PURPOSE
Real-time health status of all FKI systems: GHL, QB, Meta, Google Ads, Drive, Slack, GitHub. Single pane of glass for Squirrel operations.

## TRIGGER
Daily 5:30 AM MDT (auto) OR Bennett says "system health".

## EXECUTION STEPS
1. Check connectivity to each system:
   - GHL API: ping + last webhook timestamp
   - QuickBooks API: last successful sync
   - Meta Ads API: last data pull + token expiry
   - Google Ads API: last data pull + token expiry
   - Google Drive: file write test
   - Slack: channel post test (#leo-auto)
   - GitHub: repo access check
2. For each system:
   - GREEN: responding < 2s, no errors
   - YELLOW: slow or degraded
   - RED: unreachable or auth failure
3. RED systems: immediately post to #leo-auto with system name + error
4. Log health check to Drive: `fki-monitoring/system-health-[date].md`
5. Post daily 1-line status to #leo-auto: "Systems: GHL✅ QB✅ Meta✅ GAds✅ Drive✅"
6. Weekly: uptime % per system

## DIAMOND GATE
- T1: No system reliability claims ✅
- T2: File > 200 bytes ✅
- T3: Read-only health checks ✅
