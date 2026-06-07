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

# Detect python executable (prioritize specific Windows path, then verify commands run successfully)
if [ -f "C:/Python314/python.exe" ]; then
    PYTHON_CMD="C:/Python314/python.exe"
elif [ -f "/c/Python314/python.exe" ]; then
    PYTHON_CMD="/c/Python314/python.exe"
elif command -v python &>/dev/null && python --version &>/dev/null; then
    PYTHON_CMD="python"
elif command -v python3 &>/dev/null && python3 --version &>/dev/null; then
    PYTHON_CMD="python3"
else
    echo "Error: Python executable not found or not working."
    exit 1
fi

echo "Starting FastAPI backend with $PYTHON_CMD..."
$PYTHON_CMD -m api.main &
BACKEND_PID=$!

# Give backend a moment to initialize
sleep 2

echo "Starting Streamlit frontend with $PYTHON_CMD..."
$PYTHON_CMD -m streamlit run ui/app.py --server.port 8501 --server.headless true &
FRONTEND_PID=$!

echo "RecruitMind AI services are running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:8501"
echo "Press Ctrl+C to stop both services."

# Wait for background jobs to finish (which they won't, until killed)
wait $BACKEND_PID $FRONTEND_PID
