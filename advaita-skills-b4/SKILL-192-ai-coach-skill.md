# SKILL-192: AI Business Coach (Internal)
**Version:** 1.0 | **Pillar:** Advanced Intelligence | **Reversibility:** REVERSIBLE

## PURPOSE
Provide Bennett with AI-assisted business strategy coaching. Surfaces frameworks, challenges assumptions, pressure-tests ideas.

## TRIGGER
Bennett says "coach me on [decision/challenge]".

## EXECUTION STEPS
1. Run bennett-intelligence-layer-skill: current FKI context + priorities
2. Pull relevant data: revenue, pipeline, team capacity, market conditions
3. Apply business framework appropriate to challenge:
   - Strategic decision: 2x2 impact/effort matrix
   - Growth challenge: constraint analysis (what's the bottleneck?)
   - Pricing: value-based pricing audit
   - Team: RACI clarity check
   - Launch: pre-mortem (what could go wrong?)
4. Generate coaching response:
   - Acknowledge the challenge framing
   - Offer one contrarian perspective
   - Surface the key assumption to pressure-test
   - Provide 3 decision options with tradeoffs
5. Upload coaching session to Drive: `fki-intelligence/coaching-sessions/[date].md`
6. NO action items without Bennett explicit approval

## DIAMOND GATE
- T1: Frameworks and analysis — no financial projections ✅
- T2: File > 200 bytes ✅
- T3: Coaching document only ✅
