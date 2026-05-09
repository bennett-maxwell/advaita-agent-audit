# SKILL-144: GHL Automation Health Monitor
**Version:** 1.0 | **Pillar:** GHL Deep Automation | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor all active GHL automation workflows for failures, loops, and dead ends. Flag broken automations before they affect leads.

## TRIGGER
Daily 5 AM MDT (auto).

## EXECUTION STEPS
1. Pull GHL automation execution logs (last 24h)
2. Flag:
   - Error rate > 5% on any workflow
   - Workflow stuck in loop (same contact triggered > 3x in 1h)
   - Email delivery failures > 10%
   - Webhook failures (external integrations)
3. For each flag: generate diagnosis note
4. Critical failures: immediately post to #leo-auto with workflow name + error
5. Log daily health to Drive: `fki-ops/ghl-automation-health-[date].md`
6. Post daily green/yellow/red status to #leo-auto

## DIAMOND GATE
- T1: No claims about automation performance ✅
- T2: File > 200 bytes ✅
- T3: Monitor only ✅
