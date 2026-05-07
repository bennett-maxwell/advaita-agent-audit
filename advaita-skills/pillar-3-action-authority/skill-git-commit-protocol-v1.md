---
skill: git-commit-protocol
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI follows standard commit protocol — every change is documented, reversible, and auditable
---
# Git Commit Protocol Skill v1

## Purpose
Standardize every GitHub commit from Squirrel. Consistent format, clear messaging, proper attribution, and recovery documentation.

## Commit Message Format
```
[type]: [brief description] [Squirrel autonomous]

Types: feat (new file), fix (correction), refactor (restructure), docs (documentation), 
       audit (verification), skill (skill file update)

Examples:
feat: add franchise qualification skill v1 [Squirrel autonomous]
fix: correct FDD qualifier in IC buyer profile [Squirrel autonomous]
audit: diamond verification log batch 3 [Squirrel autonomous]
```

## Pre-Commit Checklist (all REVERSIBLE)
- [ ] Files written to disk and size-verified (T2 Recovery)
- [ ] T1 Adversarial check passed (no banned terms, FDD qualifiers present)
- [ ] T3 Boundary check: all REVERSIBLE, no external consequences from commit
- [ ] Params file used for >10 files (avoid token truncation)
- [ ] Branch: always `main` (advaita-agent-audit is Squirrel's audit repo)

## Post-Commit Verification
- Confirm SHA returned by API
- Verify `changed_paths` count matches expected file count
- Log SHA to Sprint Board and Drive receipt

## Recovery Protocol
Every commit to `main` is reversible via `git revert [SHA]`. SHA logged with every receipt.
If commit contains error: work order to Leo/Ivan for `git revert` — never force-push.

## Autonomy Value
**Replaces:** Ad hoc commits with unclear messages and no verification.
**Result:** Every commit is documented, attributable, and reversible. Audit trail always current.
**Advaita gap closed:** Version control discipline — from 0% → 100% standardized.
