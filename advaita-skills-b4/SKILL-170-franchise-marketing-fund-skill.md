# SKILL-170: Franchise Marketing Fund Manager
**Version:** 1.0 | **Pillar:** Franchise Lifecycle | **Reversibility:** REVERSIBLE

## PURPOSE
Manage SRP national marketing fund contributions and spending. FTC-compliant accounting and reporting.

## TRIGGER
Monthly 5th (auto) — after royalty collection.

## EXECUTION STEPS
1. Pull marketing fund contributions from QB (from SKILL-136 royalty data)
2. Track marketing fund expenditures:
   - National ad campaigns
   - Brand development
   - Marketing materials
3. Calculate fund balance
4. Generate FDD-compliant marketing fund report:
   - Contributions collected
   - Expenditures by category
   - Balance
5. Distribute to franchisees annually (FDD-required disclosure)
6. Log to Drive: `fki-franchise/marketing-fund-[month]-[year].md`
7. Post monthly balance to #leo-auto

## COMPLIANCE
Marketing fund accounting must be disclosed in annual FDD update.

## DIAMOND GATE
- T1: FDD-compliant reporting ✅
- T2: File > 200 bytes ✅
- T3: QB read-only. Fund distributions require Bennett legal gate ✅
