#!/bin/bash
# ═══════════════════════════════════════
# YUKI NSFW SERVER — start/stop/restart
# Usage:
#   bash nsfw_start.sh start
#   bash nsfw_start.sh stop
#   bash nsfw_start.sh restart
#   bash nsfw_start.sh status
# ═══════════════════════════════════════

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/nsfw_server.pid"
LOG_FILE="$SCRIPT_DIR/nsfw_server.log"
PYTHON="${SCRIPT_DIR}/myenv/bin/python"   # your venv python
SERVER="$SCRIPT_DIR/nsfw_server.py"
PORT="${NSFW_PORT:-7860}"

# ── Install deps if missing ────────────────────────────────────────────────────
install_deps() {
    echo "📦 Installing NSFW server dependencies..."
    $PYTHON -m pip install nudenet fastapi uvicorn pillow python-multipart --quiet
    echo "✅ Dependencies installed!"
}

# ── Start ──────────────────────────────────────────────────────────────────────
start() {
    if [ -f "$PID_FILE" ] && kill -0 "$(cat $PID_FILE)" 2>/dev/null; then
        echo "⚠️  NSFW server already running (PID $(cat $PID_FILE))"
        return
    fi

    install_deps

    echo "🚀 Starting YUKI NSFW Server on port $PORT..."
    nohup $PYTHON "$SERVER" >> "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    sleep 2

    if kill -0 "$(cat $PID_FILE)" 2>/dev/null; then
        echo "✅ NSFW Server started! PID=$(cat $PID_FILE) PORT=$PORT"
        echo "📋 Logs: tail -f $LOG_FILE"
    else
        echo "❌ Server failed to start. Check logs: $LOG_FILE"
        cat "$LOG_FILE" | tail -20
    fi
}

# ── Stop ───────────────────────────────────────────────────────────────────────
stop() {
    if [ ! -f "$PID_FILE" ]; then
        echo "⚠️  No PID file found."
        return
    fi
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
        kill "$PID"
        rm -f "$PID_FILE"
        echo "✅ NSFW Server stopped (PID $PID)"
    else
        echo "⚠️  Process $PID not running."
        rm -f "$PID_FILE"
    fi
}

# ── Status ─────────────────────────────────────────────────────────────────────
status() {
    if [ -f "$PID_FILE" ] && kill -0 "$(cat $PID_FILE)" 2>/dev/null; then
        echo "✅ Running | PID=$(cat $PID_FILE) | Port=$PORT"
        # Health check
        HEALTH=$(curl -s "http://localhost:$PORT/health" 2>/dev/null)
        echo "🔍 Health: $HEALTH"
    else
        echo "❌ Not running"
    fi
}

case "${1:-start}" in
    start)   start   ;;
    stop)    stop    ;;
    restart) stop; sleep 1; start ;;
    status)  status  ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
