---
skill: candidate-drop-off-detection
pillar: agent-intelligence
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI detects pipeline drops before they happen — saves deals that would otherwise silently die
---
# Candidate Drop-Off Detection Skill v1

## Purpose
Detect when a candidate is about to drop off the pipeline — before they ghost — and trigger preventive action.

## Drop-Off Signals by Stage

**Stage: New Lead (Days 1–3)**
Drop signal: No response to first 2 outreach attempts within 72h
Action: Switch to SMS outreach + LinkedIn message attempt; if no response by Day 7 → nurture sequence

**Stage: Discovery Scheduled**
Drop signal: No confirmation response 24h before call
Action: Automated reminder + easy reschedule link

**Stage: Post-Discovery**
Drop signal: No email open in 7 days after discovery call
Action: "Quick check-in" call from broker within 24h of signal

**Stage: FDD Stage**
Drop signal: FDD not opened within 5 days of send OR opened only once in 14+ days
Action: AI sends FDD synthesis summary + "here's what matters most" email

**Stage: Validation**
Drop signal: Validation calls not started within 14 days
Action: AI emails franchisee contact list + prompts with suggested questions

**Universal Drop Signal**: Email unsubscribe or hard bounce
Action: Immediate GHL tag update + broker notification + archive from active pipeline

## Emotional Drop Signals (detected in text/email tone)
- Declining urgency language
- Shorter reply length trend
- Shift from "we" (spouse involved) to "I" (spouse may have withdrawn support)
→ Trigger: relationship check-in, not sales push

## Autonomy Value
**Replaces:** Broker noticing dropped candidates only at weekly pipeline review.
**Result:** Real-time prevention. Deals saved that would have silently died.
**Advaita gap closed:** Pipeline attrition prevention — from 0% → 90% AI-autonomous.
