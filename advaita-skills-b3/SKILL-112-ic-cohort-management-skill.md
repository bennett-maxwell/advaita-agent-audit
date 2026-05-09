# SKILL-112: IC Cohort Management Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Automate IC coaching cohort lifecycle: weekly check-ins, progress tracking, retention alerts, graduation ceremonies.

## TRIGGER
Weekly Monday 8 AM MDT (auto) OR Bennett says "IC cohort status".

## EXECUTION STEPS
1. Pull current IC cohort list from GHL (tag: ic-enrolled)
2. Check engagement metrics:
   - Last login date (from platform API)
   - Assignments completed vs due
   - Call attendance rate
3. Flag churn risks: login > 14d OR <60% assignment completion
4. For churn risks: trigger re-engagement sequence in GHL (3-touch email + SMS)
5. For week 8+ completions: trigger graduation workflow:
   - Certificate generation (from Drive template)
   - Testimonial request email
   - Alumni upsell sequence
6. Post weekly cohort health report to #leo-auto

## DIAMOND GATE
- T1: No success rate claims ✅
- T2: File > 200 bytes ✅
- T3: Re-engagement sequences queued (not sent) pending Leo review ✅
