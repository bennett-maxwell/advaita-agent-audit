#!/bin/bash
# Machine Health Collector v2 (2026-04-29)
# v2 fix: macOS mem math — exclude `inactive` (reclaimable) from "used"
# v2 add: Slack alert when iMac mem >95% for 2+ consecutive runs
# Runs every 5 min via cron on Ivan
# Output: /Users/openclaw/.openclaw/workspace/dashboard/machine-health.json

OUTPUT="/Users/openclaw/.openclaw/workspace/dashboard/machine-health.json"
NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

pct() {
  awk -v v="$1" 'BEGIN{ v=int(v+0.5); if(v<0)v=0; if(v>100)v=100; print v }'
}

json_machine() {
  local id="$1" name="$2" ip="$3" online="$4" cpu="$5" mem="$6" disk="$7" uptime_str="$8" last_seen="$9"
  printf '{"id":"%s","name":"%s","ip":"%s","online":%s,"cpu":%s,"mem":%s,"disk":%s,"uptime":"%s","last_seen":"%s"}' \
    "$id" "$name" "$ip" "$online" "$cpu" "$mem" "$disk" "$uptime_str" "$last_seen"
}

# ── iMac (local) ─────────────────────────────────────────────────────────────

collect_imac() {
  CPU_LINE=$(top -l 2 -n 0 | grep "CPU usage" | tail -1)
  CPU_USER=$(echo "$CPU_LINE" | awk '{print $3}' | tr -d '%')
  CPU_SYS=$(echo  "$CPU_LINE" | awk '{print $5}' | tr -d '%')
  CPU_TOTAL=$(awk -v u="$CPU_USER" -v s="$CPU_SYS" 'BEGIN{printf "%d", int(u+s+0.5)}')
  CPU_TOTAL=$(pct "$CPU_TOTAL")

  VM=$(vm_stat)
  FREE=$(echo "$VM"  | awk '/Pages free/         {gsub(/\./,"",$NF); print $NF}')
  SPEC=$(echo "$VM"  | awk '/Pages speculative/  {gsub(/\./,"",$NF); print $NF}')
  WIRE=$(echo "$VM"  | awk '/Pages wired down/   {gsub(/\./,"",$NF); print $NF}')
  ACTV=$(echo "$VM"  | awk '/Pages active/       {gsub(/\./,"",$NF); print $NF}')
  INAC=$(echo "$VM"  | awk '/Pages inactive/     {gsub(/\./,"",$NF); print $NF}')
  COMP=$(echo "$VM"  | awk '/Pages occupied by compressor/ {gsub(/\./,"",$NF); print $NF}')
  # v2 fix: macOS Activity Monitor "Memory Used" = wired + active + compressed
  # `inactive` is reclaimable on demand and should NOT count as used
  USED=$((WIRE + ACTV + COMP))
  TOTAL_PAGES=$((FREE + SPEC + INAC + USED))
  MEM_PCT=0
  if [ "$TOTAL_PAGES" -gt 0 ]; then
    MEM_PCT=$(awk -v u="$USED" -v t="$TOTAL_PAGES" 'BEGIN{printf "%d", int(u/t*100+0.5)}')
  fi
  MEM_PCT=$(pct "$MEM_PCT")

  DISK_PCT=$(df -h / | awk 'NR==2 {gsub(/%/,"",$5); print $5}')
  DISK_PCT=$(pct "$DISK_PCT")

  UPTIME_STR=$(uptime | sed 's/.*up //' | sed 's/,.*//')

  # Export for alert logic
  export IMAC_MEM_PCT="$MEM_PCT"

  echo "$(json_machine "imac" "iMac" "100.103.51.12" "true" "$CPU_TOTAL" "$MEM_PCT" "$DISK_PCT" "$UPTIME_STR" "$NOW")"
}

IMAC_JSON=$(collect_imac)
IMAC_MEM_PCT=$(echo "$IMAC_JSON" | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['mem'])")

# ── MacBook (SSH) ─────────────────────────────────────────────────────────────

MACBOOK_IP="100.112.24.104"
MACBOOK_LAST_FILE="/tmp/machine-health-macbook-last.json"

collect_macbook_remote() {
  ssh -o ConnectTimeout=5 -o BatchMode=yes -o StrictHostKeyChecking=no \
      temp@${MACBOOK_IP} 'bash -s' <<'REMOTE_SCRIPT'
NOW=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

CPU_LINE=$(top -l 2 -n 0 2>/dev/null | grep "CPU usage" | tail -1)
CPU_USER=$(echo "$CPU_LINE" | awk '{print $3}' | tr -d '%')
CPU_SYS=$(echo  "$CPU_LINE" | awk '{print $5}' | tr -d '%')
CPU=$(awk -v u="$CPU_USER" -v s="$CPU_SYS" 'BEGIN{v=int(u+s+0.5); if(v<0)v=0; if(v>100)v=100; print v}')

VM=$(vm_stat)
FREE=$(echo "$VM"  | awk '/Pages free/         {gsub(/\./,"",$NF); print $NF}')
SPEC=$(echo "$VM"  | awk '/Pages speculative/  {gsub(/\./,"",$NF); print $NF}')
WIRE=$(echo "$VM"  | awk '/Pages wired down/   {gsub(/\./,"",$NF); print $NF}')
ACTV=$(echo "$VM"  | awk '/Pages active/       {gsub(/\./,"",$NF); print $NF}')
INAC=$(echo "$VM"  | awk '/Pages inactive/     {gsub(/\./,"",$NF); print $NF}')
COMP=$(echo "$VM"  | awk '/Pages occupied by compressor/ {gsub(/\./,"",$NF); print $NF}')
# v2 fix: exclude inactive (reclaimable) from used
USED=$((WIRE + ACTV + COMP))
TOTAL_PAGES=$((FREE + SPEC + INAC + USED))
MEM=0
if [ "$TOTAL_PAGES" -gt 0 ]; then
  MEM=$(awk -v u="$USED" -v t="$TOTAL_PAGES" 'BEGIN{v=int(u/t*100+0.5); if(v<0)v=0; if(v>100)v=100; print v}')
fi

DISK=$(df -h / | awk 'NR==2 {gsub(/%/,"",$5); print $5}')
UPTIME_STR=$(uptime | sed 's/.*up //' | sed 's/,.*//')

printf '{"id":"macbook","name":"MacBook","ip":"100.112.24.104","online":true,"cpu":%s,"mem":%s,"disk":%s,"uptime":"%s","last_seen":"%s"}' \
  "$CPU" "$MEM" "$DISK" "$UPTIME_STR" "$NOW"
REMOTE_SCRIPT
}

MACBOOK_JSON=$(collect_macbook_remote 2>/dev/null)
if [ $? -eq 0 ] && echo "$MACBOOK_JSON" | grep -q '"online":true'; then
  echo "$MACBOOK_JSON" > "$MACBOOK_LAST_FILE"
else
  LAST_SEEN_MB="unknown"
  if [ -f "$MACBOOK_LAST_FILE" ]; then
    LAST_SEEN_MB=$(cat "$MACBOOK_LAST_FILE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('last_seen','unknown'))" 2>/dev/null || echo "unknown")
  fi
  MACBOOK_JSON=$(json_machine "macbook" "MacBook" "$MACBOOK_IP" "false" "0" "0" "0" "offline" "$LAST_SEEN_MB")
fi

# ── Tiffany / HP Omen (HTTP Ollama) ──────────────────────────────────────────

TIFFANY_IP="100.91.17.106"
TIFFANY_LAST_FILE="/tmp/machine-health-tiffany-last.json"

json_tiffany() {
  local online="$1" model_count="$2" last_seen="$3"
  printf '{"id":"%s","name":"%s","ip":"%s","online":%s,"cpu":null,"mem":null,"disk":null,"uptime":"%s","last_seen":"%s","role":"%s","spec":"%s","metrics_available":false,"ollama_models":%s}' \
    "tiffany" "Tiffany HP Omen" "$TIFFANY_IP" "$online" "$([ "$online" = "true" ] && echo "ollama online" || echo "offline")" "$last_seen" \
    "Local AI compute node" "128GB RAM · Ollama HTTP only · no SSH" "$model_count"
}

collect_tiffany_ollama() {
  curl -fsS --connect-timeout 4 --max-time 8 "http://${TIFFANY_IP}:11434/api/tags" 2>/dev/null
}

TIFFANY_TAGS=$(collect_tiffany_ollama)
if [ $? -eq 0 ] && echo "$TIFFANY_TAGS" | grep -q '"models"'; then
  TIFFANY_MODELS=$(echo "$TIFFANY_TAGS" | python3 -c "import sys,json; print(len(json.load(sys.stdin).get('models',[])))" 2>/dev/null || echo 0)
  TIFFANY_JSON=$(json_tiffany "true" "$TIFFANY_MODELS" "$NOW")
  echo "$TIFFANY_JSON" > "$TIFFANY_LAST_FILE"
else
  LAST_SEEN_TF="unknown"
  if [ -f "$TIFFANY_LAST_FILE" ]; then
    LAST_SEEN_TF=$(cat "$TIFFANY_LAST_FILE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('last_seen','unknown'))" 2>/dev/null || echo "unknown")
  fi
  TIFFANY_JSON=$(json_tiffany "false" "0" "$LAST_SEEN_TF")
fi

# ── Write JSON ────────────────────────────────────────────────────────────────

cat > "$OUTPUT" <<EOF
{"updated":"${NOW}","machines":[${IMAC_JSON},${MACBOOK_JSON},${TIFFANY_JSON}]}
EOF

# ── v2 ADD: Slack alert when iMac mem >95% for 2+ consecutive runs ────────────

ALERT_STATE="/tmp/imac-mem-alert.state"
ALERT_THRESHOLD=95
ALERT_CHANNEL="C0AQ4KB1SA0"  # #leo-coaches

if [ -n "$IMAC_MEM_PCT" ] && [ "$IMAC_MEM_PCT" -gt "$ALERT_THRESHOLD" ]; then
  PREV=0
  [ -f "$ALERT_STATE" ] && PREV=$(cat "$ALERT_STATE" 2>/dev/null || echo 0)
  NEW=$((PREV + 1))
  echo "$NEW" > "$ALERT_STATE"
  if [ "$NEW" -eq 2 ]; then
    SLACK_TOKEN=$(grep '^SLACK_BOT_TOKEN=' /Users/openclaw/.openclaw/secrets/slack.env 2>/dev/null | cut -d= -f2- | tr -d '"' | tr -d "'")
    if [ -n "$SLACK_TOKEN" ]; then
      MSG=":warning: iMac memory at ${IMAC_MEM_PCT}% for 2 consecutive collector runs. Investigate top -o mem on 100.103.51.12. (machine-health-collector v2)"
      curl -s -X POST \
        -H "Authorization: Bearer ${SLACK_TOKEN}" \
        -H "Content-type: application/json" \
        --data "{\"channel\":\"${ALERT_CHANNEL}\",\"text\":\"${MSG}\"}" \
        https://slack.com/api/chat.postMessage > /tmp/imac-mem-alert.last 2>&1
    fi
  fi
else
  echo "0" > "$ALERT_STATE"
fi

echo "$(date): machine-health.json written OK · iMac mem ${IMAC_MEM_PCT}%"
