# SKILL-152: IC Skill Assessment Automation
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Generate structured skill assessments for IC coaching clients. Track progress objectively across the coaching engagement.

## TRIGGER
Client reaches 30-day, 60-day, or 90-day milestone in IC coaching.

## EXECUTION STEPS
1. Pull client GHL profile: enrollment date, cohort, session attendance
2. Load IC skill rubric from Drive: `fki-ic/skill-rubric.md`
   - Categories: dinking, third-shot drop, speed-up, reset, serve, return, movement, game IQ
3. Pull any Plaud session notes for skill observations
4. Generate assessment report:
   - Score each category 1-10 (based on coach notes)
   - Delta from last assessment
   - Top 2 strengths (reinforce)
   - Top 2 development areas (focus)
   - Recommended drill prescription for next 30d
5. Disclaimer: "Scores reflect coach observations. Progress varies by individual."
6. Upload to Drive: `fki-ic/assessments/[client-id]-assessment-[date].md`
7. Update GHL contact: skill_score field, last_assessment date
8. Post assessment count to #leo-auto weekly

## DIAMOND GATE
- T1: Variance disclaimer ✅
- T2: File > 200 bytes ✅
- T3: GHL field updates REVERSIBLE ✅
