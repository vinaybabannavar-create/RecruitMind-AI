# Contributing to RecruitMind AI

First off, thank you for taking the time to contribute! RecruitMind AI is an agentic candidate discovery system built to make recruiting smarter, faster, and more transparent.

To maintain code quality, robustness, and consistency, please follow these guidelines when contributing.

---

## 🛠️ Getting Started

### 1. Fork & Clone
Fork the repository on GitHub and clone your fork locally:
```bash
git clone https://github.com/your-username/RecruitMind-AI.git
cd RecruitMind-AI
```

### 2. Set Up Environment
Create a virtual environment and install all dependencies:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies including dev tools
pip install -r requirements.txt
pip install pytest pytest-cov
```

### 3. Environment Variables
Copy the `.env.example` to `.env` and configure your API keys (like `GROQ_API_KEY` if you wish to run the LLM-based parsing and explanation features).

---

## 🧪 Coding Standards & Testing

To ensure the matching engine remains reliable, we enforce strict standards:

- **Python Standards**: Follow PEP 8 guidelines. Write clean, readable code with descriptive variable/function names.
- **Type Hints**: Use type hints (e.g., `List[str]`, `Dict[str, Any]`) for all new functions.
- **Docstrings**: All modules, classes, and public functions should have clear Google-style docstrings.
- **Unit Tests**: Any modification to scoring logic, data pipeline, or core workflows must be accompanied by tests in the `tests/` directory.

### Running Tests Locally
Ensure all tests pass before proposing changes:
```bash
# Run pytest with verbose output
python -m pytest tests/ -v

# Run pytest with coverage report
python -m pytest --cov=pipeline tests/ -v
```

---

## 🚀 Pull Request Checklist

Before submitting a Pull Request, please verify:
1. [ ] **Linting & Formatting**: Your code complies with PEP 8.
2. [ ] **Test Coverage**: All existing tests pass, and you've added unit tests for new logic.
3. [ ] **CI Pipeline**: The GitHub Actions workflow (`ci.yml`) passes locally or on your branch.
4. [ ] **No Unused Imports**: Clean up debugging code, print statements, and unused libraries.
5. [ ] **Documentation**: Update `README.md` or `ARCHITECTURE.md` if your changes alter the user flow, endpoints, or database structure.

---

## 🐳 Docker Best Practices

If you modify the Docker setup:
- Keep the `Dockerfile` lightweight using multi-stage builds if needed.
- Ensure the services startup order is respected (FastAPI backend must start and load candidate vectors before the Streamlit frontend attempts to query it).
- Verify compatibility by running:
  ```bash
  docker-compose up --build
  ```
