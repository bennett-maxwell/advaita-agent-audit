# SKILL-127: Brand Voice Audit Automation
**Version:** 1.0 | **Pillar:** Brand Operations | **Reversibility:** REVERSIBLE

## PURPOSE
Audit all FKI outbound content for brand voice consistency. Flag off-brand copy before it goes live.

## TRIGGER
Bennett says "voice audit [brand]" OR weekly before content calendar goes live.

## EXECUTION STEPS
1. Pull latest content calendar from Drive: `fki-content/[brand]-calendar-current.csv`
2. Load brand voice guide: `fki-brand-voice/[brand]-voice.md`
3. Run bennett-intelligence-layer-skill for Bennett's current narrative voice
4. Score each content piece (1-10):
   - Tone match: formal/casual alignment
   - Vocabulary: brand-specific terms used correctly
   - CTA style: matches conversion strategy
   - FDD compliance: disclaimers present where needed
5. Flag scores < 7 with specific revision notes
6. Export audit report to Drive: `fki-brand/voice-audits/[brand]-[date]-audit.md`
7. Post summary (flagged count + avg score) to #leo-auto

## DIAMOND GATE
- T1: Audit only — no claims ✅
- T2: File > 200 bytes ✅
- T3: Report only, no auto-publish ✅
