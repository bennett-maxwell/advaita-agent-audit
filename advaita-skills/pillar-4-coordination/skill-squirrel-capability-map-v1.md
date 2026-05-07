---
skill: squirrel-capability-map
pillar: coordination
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: Defines what Squirrel can/cannot do — every agent knows where to route tasks
---
# Squirrel Capability Map Skill v1

## What Squirrel CAN do (cloud sandbox)
- Read and write Google Drive files
- Read and write GitHub commits
- Read and update Notion databases
- Send Slack messages to any channel
- Read GHL contact data via API
- Read QuickBooks data via API
- Read Meta Ads data via API
- Read Google Analytics data via API
- Run Python scripts and data processing
- Generate and validate content
- Run diamond verification on any content
- Build params files and execute multi-file commits
- Search knowledge base (skills, memories)
- Update Sprint Board entries
- Format and post receipts
- Execute any REVERSIBLE action listed in skill-reversible-gate-v1

## What Squirrel CANNOT do (requires Leo or Ivan)
- SSH / terminal access to any server or iMac
- Git operations requiring local machine (clone, checkout, complex rebase)
- Vercel / Convex deployment commands
- GHL actions beyond read API (some write operations requiring admin browser session)
- HeyGen browser session (video upload, account management)
- Any action requiring local file system outside sandbox
- Anything requiring persistent browser session with login state

## What Requires Bennett
- All IRREVERSIBLE financial actions (per human gate skill)
- External contract review and execution
- Identity and biometric verification
- Brand strategy decisions (new franchise, new market, pricing changes)

## Routing Decision Tree
Task comes in → Is it in Squirrel CAN list? → YES: execute → NO: Is it in Leo/Ivan list? → YES: work order → NO: Human Gate

## Autonomy Value
**Replaces:** Agents wasting time trying to do things outside their capability or asking what to do.
**Result:** Every agent knows exactly where each task belongs. Zero routing confusion.
**Advaita gap closed:** Agent routing clarity — from 0% → 100%.
