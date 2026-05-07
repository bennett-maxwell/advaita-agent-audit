---
skill: leo-capability-map
pillar: coordination
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: Defines Leo's capabilities — Squirrel routes correctly every time, no guessing
---
# Leo Capability Map Skill v1

## What Leo CAN do (iMac orchestrator)
- Execute terminal/CLI commands on local iMac
- Run git commands (clone, checkout, push, revert, complex operations)
- SSH to any connected server
- Run Vercel/Convex/server deployment commands
- Maintain persistent browser sessions (Chrome, logged-in sessions)
- Execute GHL admin operations requiring browser
- Run local Python/Node scripts outside sandbox
- Manage cron jobs and scheduled tasks on iMac
- Monitor local system resources

## Leo's Slack Identity
- User ID: U0AG6G4BEM9
- Always @mention Leo in #leo-auto (C0AKXT2S1T2) for work orders
- Leo only activates on @mention in #leo-auto (per BUG-006 fix)
- appToken A0AV30H37QE active for Leo's Slack connection

## Leo Work Order Format
Use skill-work-order-formatter-v1. Tag @Leo. Include WO-[ID].
Expected SLA: P1 same session / P2 today / P3 this week

## Leo's Known Limitations
- Cannot execute cloud API calls that require Squirrel's integration tokens
- Cannot access Squirrel's GHL/QB/Meta API connections
- Routes cloud API tasks back to Squirrel

## Coordination Protocol
Squirrel → Leo work order → Leo executes → Leo posts receipt → Squirrel confirms → Sprint Board updated

## Autonomy Value
**Replaces:** Squirrel trying to do CLI work (impossible) or Leo being asked for cloud API work (wrong tool).
**Result:** Fleet runs at maximum efficiency. Each agent does what only they can do.
**Advaita gap closed:** Leo routing accuracy — from 0% → 100%.
