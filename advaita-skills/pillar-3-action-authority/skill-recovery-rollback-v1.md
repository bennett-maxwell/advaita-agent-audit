---
skill: recovery-rollback-protocol
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI knows how to undo every REVERSIBLE action — zero permanent mistakes, maximum trust
---
# Recovery and Rollback Protocol Skill v1

## Purpose
For every category of REVERSIBLE action, define the exact rollback procedure. AI can recover from any mistake without human intervention for REVERSIBLE actions.

## Rollback Procedures by Action Type

**GitHub Commit Rollback**
Trigger: Wrong files committed, content error discovered post-commit
Procedure: Work order to Leo → `git revert [SHA]` → commit revert → post receipt
Note: Never force-push main. Always revert, never reset.

**Google Drive File Rollback**
Trigger: Wrong content saved, file saved to wrong folder
Procedure: Delete or overwrite file via GOOGLEDRIVE_DELETE_FILE or create replacement
Note: Drive files can be trashed and restored within 30 days

**Notion Update Rollback**
Trigger: Wrong Sprint Board entry, incorrect status
Procedure: Update property directly via Notion API → restore correct values

**GHL Tag/Stage Rollback**
Trigger: Wrong tag applied, stage incorrectly advanced
Procedure: Remove tag via GHL API, revert stage to prior stage

**Slack Message Rollback**
Trigger: Wrong information posted to channel
Procedure: Use SlackDeleteMessage (bot messages only) or post correction message with "CORRECTION: [prior message corrected]"

## Recovery Documentation (always log)
When rollback is executed:
```
## RECOVERY-[YYYYMMDD]-[NNN]
Original action: [what was done incorrectly]
Error discovered: [when and how]
Rollback performed: [exact steps taken]
Current state: [confirmed correct state]
Prevention: [what will prevent recurrence]
```

## Autonomy Value
**Replaces:** Mistakes becoming permanent because no recovery protocol exists.
**Result:** AI can operate with confidence knowing every REVERSIBLE action can be undone cleanly.
**Advaita gap closed:** Error recovery capability — from 0% → 100% defined.
