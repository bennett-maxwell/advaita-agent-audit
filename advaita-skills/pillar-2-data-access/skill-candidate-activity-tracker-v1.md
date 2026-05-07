---
skill: candidate-activity-tracker
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI tracks all candidate activity across channels — complete engagement picture without manual monitoring
---
# Candidate Activity Tracker Skill v1

## Purpose
Build a real-time activity timeline for every active candidate across all touchpoints: email, calls, website visits, GHL activity. Complete engagement picture at all times.

## Activity Data Sources (all REVERSIBLE — read-only)

**Email Activity (GHL)**
- Emails sent, opened, clicked (timestamp + which email)
- Reply received (triggers broker notification)
- Unsubscribe or bounce (triggers pipeline update)

**Call Activity (GHL + calendar)**
- Calls logged, duration, outcome (from call log)
- Meetings scheduled / completed (from calendar sync)
- Voicemails left (from call log)

**Website Activity (GA4 → GHL)**
- Pages visited (which content, how long)
- Return visits (high intent signal)
- Specific pages: FDD info, investment range, specific brand pages

**Form Activity (GHL)**
- Forms submitted (intake, consultation request, download)
- Fields completed vs. skipped (indicates hesitation areas)

## Activity Score (0–100, recalculated daily)
Weight: recent activity > older activity. Engagement with brand-specific content = higher signal.

## CLOSE NOW Signal Integration
When activity score spikes (>20 point increase in 7 days): trigger closing signal detection (skill-closing-signal-detection-v1).

## Autonomy Value
**Replaces:** Broker checking email, CRM, and calendar separately to understand candidate engagement.
**Result:** Single unified activity view for every candidate. High-intent moments never missed.
**Advaita gap closed:** Candidate engagement visibility — from 0% → 100% AI-autonomous.
