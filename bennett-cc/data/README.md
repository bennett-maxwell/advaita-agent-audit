# bennett-cc/data — JSON feeds for the FKI Command Center

The dashboard at `https://dashboard.franchiseki.com/bennett-cc/` fetches these files every page-load and every 5 minutes (auto-refresh).

| File | Producer | Consumer | Refresh |
|------|----------|----------|---------|
| `machines.json` | `~/.openclaw/workspace/dashboard/machine-health-collector.sh` (Ivan, cron */5 min) | Tech tab → Computer Health | 5 min |
| `tailscale.json` | `bennett-cc-data-sync.sh` → `tailscale status --json` (Ivan) | Tech tab → Tailscale Mesh | 5 min |
| `pulse.json` | `pulse-skill` writes `~/.openclaw/workspace/dashboard/pulse-data.json` → sync script copies | Marketing tab (CPA/CPL/Pipeline/Social) | per pulse run |

## Sync script

`/Users/openclaw/.openclaw/workspace/dashboard/bennett-cc-data-sync.sh` (Ivan)

Runs every 5 minutes. Copies live JSON from `workspace/dashboard/` into `repo/bennett-cc/data/`, then `git add + commit + push` if any file changed. GitHub Pages picks up changes within ~1 minute.

## Wiring pulse-skill (TODO)

`pulse-skill` currently emails Bennett but does not write `pulse-data.json`. Add this step at end of pulse run:

```python
# pulse-skill: at end of build_pulse_payload()
import json, pathlib
out = pathlib.Path('/Users/openclaw/.openclaw/workspace/dashboard/pulse-data.json')
out.write_text(json.dumps({
    'updated': datetime.utcnow().isoformat() + 'Z',
    'cpa_booked': {...},     # by brand
    'cpa_shown':  {...},
    'cpl':        {...},
    'pipeline':   {...},     # total_leads_in, call_1s, call_2s, total_calls
    'stages':     {...},     # by stage: count + names[]
    'social':     {...},     # by platform: views_7d, delta_pct, engagement_7d
}, indent=2))
```

The next `bennett-cc-data-sync.sh` cycle will commit + push it automatically.
