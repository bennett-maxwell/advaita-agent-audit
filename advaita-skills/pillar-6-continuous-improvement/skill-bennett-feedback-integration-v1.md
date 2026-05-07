---
skill: bennett-feedback-integration
pillar: continuous-improvement
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI captures every correction from Bennett and integrates it — every "no" makes AI smarter
---
# Bennett Feedback Integration Skill v1

## Purpose
Every time Bennett corrects, redirects, or improves on something AI did, that signal is captured and integrated into the knowledge base. AI gets smarter with every interaction.

## Feedback Detection Triggers

**Explicit Corrections**: "No, do it this way instead" / "That's wrong — it should be X"
→ Capture: what AI did, what Bennett corrected it to, the principle behind the correction

**Preference Signals**: "I like this format better" / "Always do X this way going forward"
→ Capture: preference + context + when it applies

**Approval Signals**: "Yes, exactly" / "This is perfect" / "Keep doing it this way"
→ Capture: what worked, why it resonated, replicate the approach

**Implicit Signals**: Bennett significantly editing an AI output before using it
→ Capture: what changed + likely reason

## Integration Actions (REVERSIBLE)

For corrections → create/update Memory draft with new rule or fact
For preferences → create/update Memory draft with preference + whenToUse
For skill improvements → flag specific skill for update, queue to weekly skill audit
For process improvements → update relevant skill documentation

## Feedback Log (Drive .learnings/bennett-feedback.md)
```
## FEEDBACK-[YYYYMMDD]-[NNN]
Context: [what AI was doing]
Feedback type: CORRECTION / PREFERENCE / APPROVAL / IMPLICIT
Signal: [what Bennett said or did]
Principle: [the generalizable rule extracted from this feedback]
Action taken: [memory created / skill updated / approach noted]
```

## Autonomy Value
**Replaces:** AI making the same mistakes repeatedly because feedback isn't captured.
**Result:** Every Bennett interaction makes the AI more aligned with Bennett's preferences. Over time, corrections become rare because the AI has internalized the right approach.
**Advaita gap closed:** AI personalization and alignment — from 0% → 90% systematic learning.
