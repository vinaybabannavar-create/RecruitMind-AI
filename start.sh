#!/bin/bash
# start.sh — Production startup script for Render (Single Free Web Service)

# 1. Generate candidates dataset if missing
python data/generate_candidates.py

# 2. Start FastAPI backend in background on port 8000
echo "Starting FastAPI backend on port 8000..."
uvicorn api.main:app --host 127.0.0.1 --port 8000 &

# 3. Wait 3 seconds for backend to start up
sleep 3

# 4. Start Streamlit frontend on Render's assigned $PORT
PORT=${PORT:-8501}
echo "Starting Streamlit frontend on port $PORT..."
exec streamlit run ui/app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true
