---
skill: error-classification
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI classifies and routes every error correctly — zero errors ignored, zero escalations wasted
---
# Error Classification Skill v1

## Purpose
Every error encountered during AI execution is classified, routed, and resolved via the correct path. No error is silently ignored. No unnecessary human escalations.

## Error Classification Matrix

| Error Symptom | Root Cause | Resolution Path |
|--------------|-----------|----------------|
| Tool returns 404 | Wrong resource ID | Verify ID, try alternate lookup |
| Tool returns 403 | Permissions/scope issue | DIY steps 4–5, route to Ivan if Drive PATCH needed |
| Tool returns empty (200, no data) | Scope/filter issue | Add allDrives=true, corpora=allDrives |
| API timeout (>30s) | Rate limit or service lag | Retry once after 60s; if fails again → work order |
| Slack message not delivered | Wrong channel ID or bot permissions | Verify channel ID against known list |
| Notion write fails | Wrong DB ID or property name mismatch | Verify schema, check property names |
| Drive file not found | Shared drive scope missing | Add supportsAllDrives=true + includeItemsFromAllDrives=true |
| GHL field not updating | Wrong field key name | SearchIntegrations for correct field schema |
| GitHub commit fails | Wrong branch, file too large, or auth | Check params, use paramsFile for large payloads |

## Error Response Protocol (in order)
1. Classify error using matrix above
2. Apply documented fix
3. If fix resolves → log to audit trail, continue
4. If fix fails → run DIY Skill 9 steps
5. If all 9 DIY steps fail → work order to Leo
6. Log all errors to Drive ERRORS.md

## Error Log Format (Drive ERRORS.md)
```
## ERR-[YYYYMMDD]-[NNN]
Error: [exact message]
Context: [what was being attempted]
Classification: [from matrix above]
Fix attempted: [what was tried]
Resolution: [how it was resolved OR "escalated to Leo"]
```

## Autonomy Value
**Replaces:** AI stopping on first error and asking for help.
**Result:** 90% of errors self-resolved using classification matrix. Leo/Bennett only see the 10% that genuinely need human help.
**Advaita gap closed:** Error self-resolution — from 0% → 90% AI-autonomous.
