# SKILL-121: Cross-Brand Upsell Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Identify IC/SH clients who qualify for SRP or cross-brand offers. Trigger targeted upsell sequences without Bennett manual review.

## TRIGGER
Weekly Wednesday 8 AM MDT (auto).

## EXECUTION STEPS
1. Pull all enrolled clients across IC, SH, SRP from GHL
2. Score cross-brand fit:
   - IC-enrolled + business owner tag → SH candidate
   - SH-enrolled + sports background → IC candidate
   - IC or SH high-LTV + entrepreneur tag → SRP franchise candidate
3. For top 10 cross-brand matches:
   - Generate personalized transition email (brand voice via bennett-intelligence-layer-skill)
   - Add FDD qualifier if SRP offer mentioned
4. Queue emails in GHL (not sent — Leo review required)
5. Post cross-brand opportunity list to #leo-auto

## DIAMOND GATE
- T1: FDD qualifiers on all SRP mentions. No income claims ✅
- T2: File > 200 bytes ✅
- T3: Emails queued not sent ✅
