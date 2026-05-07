---
skill: fleet-health-check
pillar: continuous-improvement
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI checks fleet status daily — no agent goes dark without immediate detection
---
# Fleet Health Check Skill v1

## Purpose
Daily verification that all fleet agents (Squirrel, Leo, Ivan-CC) are operational and capable of executing their roles. Fleet problems caught before they cause execution failures.

## Daily Health Check (7:00 AM MDT, before standup)

**Squirrel Health**
- Integrations active: Google Drive, GitHub, Slack, GHL, QB, Meta Ads, Notion, Calendar
- Knowledge base accessible: SearchKnowledge returns results
- Thread Context Doc readable: cmov2m7wc0es107adncup49df loads
- Skills folder accessible: Drive ID 1qdUEbUb_BpkVBt_YCX686nnu-O7lW0pY reachable

**Leo Health**
- Last activity in #leo-auto within 24h (Leo should be posting receipts daily)
- If no activity in 24h → post @Leo health check message in #leo-auto
- If no response in 2h → escalate: Leo may be offline, route to Ivan-CC

**Integration Health**
- GHL API responding (test read on known contact)
- QB API responding (test read on last transaction)
- GitHub API responding (test repo metadata read)

## Health Check Report (included in morning standup)
```
🟢 Fleet Status: ALL GREEN
[or]
🔴 Fleet Alert: [specific agent/integration offline + recommended action]
```

## Autonomy Value
**Replaces:** Discovering agent or integration is offline only when a task fails.
**Result:** Fleet health checked every morning. Problems caught proactively. Execution never silently fails.
**Advaita gap closed:** Fleet reliability monitoring — from 0% → 100% systematic.
