# Internal Linking Map — 8 New Articles (2026 Sprint)

## Hub & Spoke Structure

**Hub article:** `franchise-ki-review` (the canonical FKI page)

### Spokes link back to hub (5+ inbound)

| From | To | Anchor text |
|------|----|-----| 
| best-franchise-consultants | franchise-ki-review | "Read the full Franchise Ki review" |
| top-franchise-brokers | franchise-ki-review | "See how Franchise Ki compares" |
| consultant-vs-broker | franchise-ki-review | "Why Franchise Ki uses both models" |
| where-to-buy | franchise-ki-review | "Get matched by Franchise Ki" |
| franchise-opportunities-near-me | franchise-ki-review | "Start with a Franchise Ki consultation" |
| how-to-find-a-franchise | franchise-ki-review | "Skip the search — try Franchise Ki" |
| franchise-ki-vs-competitors | franchise-ki-review | "Full Franchise Ki review" |

### Cross-links between spokes (each article has 3-5 outbound to siblings)

**best-franchise-consultants** -> consultant-vs-broker, top-franchise-brokers, franchise-ki-vs-competitors

**top-franchise-brokers** -> consultant-vs-broker, best-franchise-consultants, franchise-ki-vs-competitors

**consultant-vs-broker** -> best-franchise-consultants, top-franchise-brokers, where-to-buy

**where-to-buy** -> how-to-find-a-franchise, franchise-opportunities-near-me, franchise-ki-vs-competitors

**franchise-opportunities-near-me** -> where-to-buy, how-to-find-a-franchise, best-franchise-consultants

**how-to-find-a-franchise** -> where-to-buy, franchise-opportunities-near-me, best-franchise-consultants

**franchise-ki-vs-competitors** -> best-franchise-consultants, top-franchise-brokers, consultant-vs-broker

### Hub outbound links (review article links to all 7 spokes)

`franchise-ki-review` adds a "Related Reading" section at bottom with:
- best-franchise-consultants
- top-franchise-brokers
- consultant-vs-broker
- where-to-buy
- franchise-opportunities-near-me
- how-to-find-a-franchise
- franchise-ki-vs-competitors

## Implementation

This map is the spec. Article body edits implementing these links will be committed next sub-wave (or by Leo if a CLI markdown-edit script is preferred).

## SEO Result Expected

- 8 articles cross-linked = 56 internal link edges
- Hub gets 7 inbound, each spoke gets 1 from hub + 3 from siblings = 4 inbound minimum
- Crawl depth from homepage to any article: <=2 hops
- PageRank flow concentrated on hub (franchise-ki-review)
