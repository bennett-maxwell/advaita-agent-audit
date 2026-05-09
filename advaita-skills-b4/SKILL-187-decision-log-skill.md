# SKILL-187: Decision Log Automation
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Log every significant operational decision made by FKI agents and track outcomes. Builds institutional memory and accountability.

## TRIGGER
After any SKILL execution that modifies external state (campaigns launched, emails queued, configs changed).

## EXECUTION STEPS
1. On trigger: capture decision record:
   - Timestamp (MDT)
   - Skill that executed
   - Decision made (what action was taken or recommended)
   - Inputs used
   - Agent: Squirrel / Leo / Madison
2. Append to Drive: `fki-intelligence/decision-log-[month]-[year].md`
3. Weekly: review decisions with unexpected outcomes (deviation from expected ROAS/conversion)
4. For outcome deviations > 20%: generate "post-mortem note" in same log
5. Monthly: pattern analysis (SKILL-186) uses decision log as input
6. Post weekly decision count to #leo-auto (count only, no details)

## DIAMOND GATE
- T1: Historical record only ✅
- T2: File > 200 bytes ✅
- T3: Append-only log ✅
