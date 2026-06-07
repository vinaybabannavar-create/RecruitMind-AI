#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo ""
    echo "Stopping background services..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Trap SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

echo "Starting FastAPI backend..."
python api/main.py &
BACKEND_PID=$!

# Give backend a moment to initialize
sleep 2

echo "Starting Streamlit frontend..."
streamlit run ui/app.py --server.port 8501 --server.headless true &
FRONTEND_PID=$!

echo "RecruitMind AI services are running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:8501"
echo "Press Ctrl+C to stop both services."

# Wait for background jobs to finish (which they won't, until killed)
wait $BACKEND_PID $FRONTEND_PID
