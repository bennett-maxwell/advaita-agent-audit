# SKILL-154: SH Revenue Tracking Automation
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Track Smash Hotel client revenue milestones against benchmarks. Flag overperformers for case studies, underperformers for intervention.

## TRIGGER
Weekly Wednesday 8 AM MDT (auto).

## EXECUTION STEPS
1. Pull SH enrolled clients from GHL (tag: sh-enrolled)
2. For each client: pull revenue data from QB sync or client-reported milestone
3. Compare to SH benchmark timeline from Drive: `fki-sh/revenue-benchmarks.md`
4. Categorize:
   - Ahead of benchmark: flag for testimonial/case study request
   - On track: no action
   - Behind benchmark (>25%): trigger intervention check-in
5. For intervention clients: draft personal email from Bennett template
6. Log milestone data to Drive: `fki-sh/revenue-tracking-[date].md`
7. Post weekly cohort milestone summary to #leo-auto

## COMPLIANCE
All client revenue data handled confidentially. Benchmarks are targets, not guarantees.
"Revenue benchmarks are not a guarantee of results. Individual results vary based on effort, market conditions, and execution."

## DIAMOND GATE
- T1: Benchmarks labeled as targets not guarantees. FDD qualifier ✅
- T2: File > 200 bytes ✅
- T3: Intervention emails queued not sent ✅
