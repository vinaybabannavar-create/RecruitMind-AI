#!/bin/bash
# start.sh — Startup script for Render (Docker) deployment
# Runs FastAPI backend internally on 8000 + Streamlit on Render's $PORT

set -e

# Generate candidates dataset if missing
if [ ! -f "data/candidates.json" ]; then
    echo "Generating candidates dataset..."
    python data/generate_candidates.py
fi

# Start FastAPI backend in background on internal port 8000
echo "Starting FastAPI backend on port 8000..."
uvicorn api.main:app --host 127.0.0.1 --port 8000 &

# Give backend a moment to boot
sleep 4

# Start Streamlit on Render's assigned $PORT (default 8501 for local)
PORT=${PORT:-8501}
echo "Starting Streamlit frontend on port $PORT..."
exec streamlit run ui/app.py \
    --server.port $PORT \
    --server.address 0.0.0.0 \
    --server.headless true \
    --server.enableCORS false
