---
skill: ghl-pipeline-updater
pillar: data-access
version: 1.0
diamond: T1-PASS T2-PASS T3-PASS REVERSIBLE
advaita_gap: AI updates GHL pipeline stages automatically — CRM always current without manual entry
---
# GHL Pipeline Stage Updater Skill v1

## Purpose
Automatically advance GHL pipeline stages based on detected events and behavioral signals. CRM is always current — no broker data entry required.

## Stage Advancement Rules (all REVERSIBLE — GHL tag/stage changes)

| Trigger Event | Stage Change |
|--------------|-------------|
| Discovery call completed (calendar event marked done) | Prospects → Post-Discovery |
| FDD email sent by broker or AI | Post-Discovery → FDD Review |
| Validation call scheduled (calendar event created) | FDD Review → Validation |
| Award decision verbal commitment | Validation → Pending Award |
| Franchise agreement signed | Pending Award → Awarded |
| Training start date confirmed | Awarded → In Training |
| Grand opening date set | In Training → Open |

## Stage Regression Rules (REVERSIBLE)
If candidate goes 30 days without progress → apply stall tag + generate broker alert
If candidate explicitly requests pause → apply `candidate-paused` tag + schedule check-in

## GHL Activity Notes (auto-added on each stage change)
"Stage advanced to [X] on [date] by Squirrel AI. Trigger: [event]. Next: [recommended action]."

## Autonomy Value
**Replaces:** Broker manually dragging pipeline cards in GHL after every interaction.
**Result:** GHL is always accurate. Reporting is always real-time. Broker never opens CRM to "update" — only to communicate.
**Advaita gap closed:** CRM maintenance — from 0% → 100% AI-autonomous.
