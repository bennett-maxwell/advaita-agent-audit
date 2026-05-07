---
skill: drive-write-protocol
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI follows Drive write protocol — files always in right folder, correctly named, never lost
---
# Google Drive Write Protocol Skill v1

## Purpose
Standardize every Google Drive write from Squirrel. Right folder, right name, right format. Files always findable by any agent or Bennett.

## Folder Routing Rules

| Content Type | Drive Folder ID | Folder Name |
|-------------|-----------------|-------------|
| Skill files | 1qdUEbUb_BpkVBt_YCX686nnu-O7lW0pY | Skills (canonical) |
| Diamond logs | 1qdUEbUb_BpkVBt_YCX686nnu-O7lW0pY | Skills folder |
| Audit reports | 1qdUEbUb_BpkVBt_YCX686nnu-O7lW0pY | Skills folder |
| Error logs | Drive skills folder `.learnings/` subfolder | Errors |

## File Naming Convention
```
[content-type]-[descriptor]-[YYYYMMDD].md

Examples:
diamond-verification-batch3-20260507.md
skill-lead-qualification-v1.md
audit-report-weekly-20260507.md
error-log-20260507.md
```

## Write Tool Parameters
Always include for Drive folder writes:
- `name`: [file name with .md extension]
- `mimeType`: text/markdown OR text/plain
- `parents`: [folder ID from routing table above]
- `text_content`: [file content] (NOT `fileContent` — that's the wrong field name)

## Post-Write Verification
Confirm file ID returned in response.
Log file ID to Sprint Board entry for that task.
If write fails: retry once with same params; if still fails → work order to Leo.

## Autonomy Value
**Replaces:** Ad hoc Drive saves with inconsistent naming and locations.
**Result:** Every file findable by any agent at any time. Knowledge base always organized.
**Advaita gap closed:** Knowledge management hygiene — from 0% → 100% standardized.
