---
skill: commission-calculator
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI calculates commissions automatically — replaces manual commission tracking
---
# Commission Calculator Skill v1

## Purpose
Automatically calculate and track franchise broker commissions when a deal closes. Eliminates manual spreadsheet tracking and ensures nothing is missed.

## Commission Tracking Triggers
Trigger: GHL stage → "Awarded" OR broker reports close to Squirrel

## Commission Calculation Logic (REVERSIBLE — tracking only)

**Data required**:
- Brand awarded
- Territory/market
- Franchisor confirmation of commission rate (varies by brand — confirm at time of award)
- Broker who closed the deal
- Referral source (if referral commission applies)

**Commission note**: Actual commission rates are franchisor-specific and confirmed at award. AI tracks the record; actual payment reconciliation requires franchisor invoice (IRREVERSIBLE financial action → Bennett gate).

## Commission Tracking Record (saved to Drive after each close)
```
Close Date: [date]
Candidate: [name, redacted in shared logs]
Brand: [brand name]
Territory: [market]
Broker: [name]
Estimated Commission: per franchisor rate (results vary by brand/deal)
Referral Credit: [if applicable]
Franchisor Invoice: PENDING / RECEIVED / PAID
Status: TRACKING
```

## Monthly Commission Summary (posted to #leo-auto, 1st of month)
- Deals closed in prior month
- Commissions tracked (estimates — actual per franchisor invoices)
- Outstanding invoices
- YTD tracking total (estimate — consult accountant for financial decisions)

## Autonomy Value
**Replaces:** Manual commission spreadsheet tracking.
**Result:** Every close is tracked automatically. No commission missed. Monthly summary is always ready.
**Advaita gap closed:** Revenue tracking automation — from 0% → 90% AI-autonomous (financial reconciliation still requires human gate).
