---
skill: preflight-content-check
pillar: action-authority
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI runs preflight check before any content publish — replaces manual review before going live
---
# Preflight Content Check Skill v1

## Purpose
Final gate before ANY content goes public. AI runs full preflight checklist. Content that fails preflight never publishes. Period.

## Preflight Checklist (all must pass)

- [ ] Legal compliance gate (skill-legal-compliance-gate-v1) — PASS required
- [ ] No banned entity names present
- [ ] All dollar amounts have FDD qualifiers
- [ ] State block check passed for all brand × state combinations in content
- [ ] Brand language correct (IC = community hub, not thrift store)
- [ ] No forward-looking income projections without FDD qualifier
- [ ] Real photo used as base if showing brand location (not AI-generated from text alone)
- [ ] Video content: B-roll at 2–5s and 5–8s marks
- [ ] Video content: at least one Item 19 figure cited if financial claims present
- [ ] Content tone aligns with brand (IC: community-first; SH: investor/ROI-oriented; SRP: memory/family)

## Preflight Result
ALL PASS → content approved for publish (REVERSIBLE: still log for audit trail)
ANY FAIL → content BLOCKED. Specific failure noted. Fix required before re-preflight.

## Preflight Log
Every preflight result logged: date, content type, checks run, result, action.

## Autonomy Value
**Replaces:** Human review before each publish.
**Result:** Every piece of content that goes live has been AI-verified for compliance. Legal risk at zero.
**Advaita gap closed:** Pre-publish verification — from 0% → 100% AI-autonomous.
