# SKILL-159: SRP Vendor Management Automation
**Version:** 1.0 | **Pillar:** Brand Playbooks | **Reversibility:** REVERSIBLE

## PURPOSE
Monitor SRP approved vendor relationships. Track pricing, contract renewals, and preferred supplier performance.

## TRIGGER
Monthly 10th (auto) OR Bennett says "vendor review".

## EXECUTION STEPS
1. Pull SRP approved vendor list from Drive: `fki-franchise/approved-vendors.md`
2. Check contract expiry dates — flag any expiring within 60 days
3. Pull franchisee purchasing data (from QB) — verify purchases from approved vendors only
4. Flag: franchisees purchasing from non-approved vendors > 10% of category spend
5. Generate vendor performance scorecard:
   - Delivery reliability (franchisee reported)
   - Price competitiveness
   - Product quality (NPS-based)
6. Recommend: remove low-scoring vendors from approved list (> 3 months data)
7. Upload to Drive: `fki-franchise/vendor-scorecard-[date].md`
8. Post summary to #leo-auto

## DIAMOND GATE
- T1: No vendor performance guarantees ✅
- T2: File > 200 bytes ✅
- T3: Recommendations only — Leo approves vendor changes ✅
