---
skill: memory-update-protocol
pillar: continuous-improvement
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI maintains its own memory — institutional knowledge always current and accessible
---
# Memory Update Protocol Skill v1

## Purpose
Define when and how AI updates its persistent memory. Memories make AI smarter over time — they should be created whenever new important information is learned.

## Memory Creation Triggers

**Create New Memory When:**
- Bennett corrects a fact ("Actually, that's X not Y")
- A new preference is expressed ("Always format receipts with X")
- A new constraint is discovered ("We don't work with [category] franchisors")
- A new workflow decision is made ("Going forward, always do X before Y")
- A new team member, brand, or key entity is introduced
- A key number or metric is established (target, benchmark, threshold)

**Update Existing Memory When:**
- A fact previously memorized has changed
- A preference has shifted
- A constraint has been updated

## Memory Categories
- `user_fact`: Facts about Bennett or FKI that persist
- `preference`: How Bennett wants things done
- `project_context`: Active project state
- `domain_knowledge`: FKI industry and brand knowledge
- `tools_and_workflows`: How specific tools work in FKI context

## Memory Creation Format
When creating a memory draft:
- Content: specific, actionable fact (not vague)
- Category: one of the above
- Importance: 1–10 (1=low, 10=critical)
- whenToUse: when should this memory surface?

## Memory Review Schedule
Monthly: Review all memories for staleness. Deprecate outdated ones.

## Autonomy Value
**Replaces:** Squirrel forgetting key facts between sessions and being re-briefed.
**Result:** Memory compounds over time. AI becomes increasingly effective with each interaction.
**Advaita gap closed:** Institutional knowledge persistence — from 0% → 90% systematic.
