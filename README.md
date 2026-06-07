# 🧠 RecruitMind AI

> **Next-Generation Agentic Talent Discovery Platform**  
> Built for the **Redrob AI Hackathon 2026**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_Pipeline-6C63FF?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Search-F97316?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Llama--3.3-22C55E?style=for-the-badge)

</div>

---

## 🚀 Overview

**RecruitMind AI** is a fully agentic AI-powered recruitment intelligence platform that transforms how talent is discovered, evaluated, and shortlisted. Instead of simple keyword matching, it uses a multi-signal scoring engine backed by semantic vector search, LLM-generated recruiter notes, and explainable AI reasoning to surface the *best-fit* candidates for any job description.

### ✨ Key Highlights

- 🔍 **Cognitive JD Parsing** — LLM extracts skills, seniority, culture fit, and implicit requirements
- 📊 **Multi-Signal Scoring Engine** — Composite scores across 5 independent signals
- 💡 **Explainable AI Shortlists** — Natural language recruiter notes per candidate (Groq Llama-3.3)
- 🎯 **Semantic Vector Search** — ChromaDB + Sentence Transformers (all-MiniLM-L6-v2)
- ⚡ **LangGraph Agentic Pipeline** — Modular, stateful ranking pipeline
- 🎨 **Premium Cinematic UI** — Full-screen animated splash, glassmorphism dashboard

---

## 🏗️ Architecture

```
recruitmind-ai/
│
├── api/                    # FastAPI REST backend
│   ├── main.py             # API routes: /health, /rank, /index
│   └── __init__.py
│
├── pipeline/               # LangGraph agentic pipeline
│   ├── graph.py            # LangGraph state machine
│   ├── nodes.py            # Pipeline nodes (parse, embed, rank, explain)
│   ├── ranker.py           # Multi-signal scoring engine
│   ├── embedder.py         # Sentence Transformers wrapper
│   ├── vector_store.py     # ChromaDB vector store
│   ├── llm_client.py       # Groq Llama-3.3 client
│   └── __init__.py
│
├── data/                   # Candidate data
│   └── candidates.json     # Sample candidate profiles (50+ candidates)
│
├── ui/                     # Streamlit premium dashboard
│   ├── app.py              # Main Streamlit app (splash + dashboard)
│   └── logo.png            # RecruitMind AI logo
│
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build
├── docker-compose.yml      # Multi-service orchestration
└── README.md
```

---

## 🔬 Multi-Signal Scoring Engine

| Signal | Weight | Description |
|--------|--------|-------------|
| **Semantic Similarity** | 35% | Cosine similarity via ChromaDB vector search |
| **Skill Match** | 30% | Matched skills vs. JD required skills |
| **Career Growth** | 15% | Trajectory & progression signals |
| **Activity Signal** | 10% | Recency, open-source, certifications |
| **Experience Fit** | 10% | Years experience vs. JD requirements |

**Final composite score = weighted sum** → sorted descending → top-K returned

---

## 🧠 LangGraph Agentic Pipeline

```
[JD Input]
    │
    ▼
[parse_jd_node]      ← LLM extracts: skills, title, seniority, experience
    │
    ▼
[embed_jd_node]      ← Sentence Transformer embeds the JD
    │
    ▼
[vector_search_node] ← ChromaDB retrieves top-N similar candidates
    │
    ▼
[rank_candidates_node] ← Multi-signal composite scoring
    │
    ▼
[explain_node]       ← Groq Llama-3.3 writes recruiter notes
    │
    ▼
[output]             ← JSON: ranked shortlist + metadata + explanations
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.12+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### 1. Clone the repository

```bash
git clone https://github.com/vinaybabannavar-create/-RecruitMind-AI.git
cd -RecruitMind-AI
```

### 2. Create virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 5. Index candidates

```bash
# Start FastAPI backend first, then:
curl -X POST http://localhost:8000/index \
  -H "Content-Type: application/json" \
  -d '{"candidates_path": "data/candidates.json"}'
```

---

## 🚀 Running the Application

### Start FastAPI Backend (Terminal 1)

```bash
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

### Start Streamlit UI (Terminal 2)

```bash
streamlit run ui/app.py --server.port 8501
```

Open **http://localhost:8501** in your browser.

### Or use Docker Compose

```bash
docker-compose up --build
```

---

## 📡 API Reference

### `POST /rank`

Rank candidates for a given job description.

**Request:**
```json
{
  "jd_text": "Senior Python ML Engineer with LangChain, FastAPI, Docker, 4+ years",
  "top_k": 10,
  "with_explanations": true
}
```

**Response:**
```json
{
  "shortlist": [
    {
      "rank": 1,
      "name": "Candidate Name",
      "composite_score": 0.87,
      "score_breakdown": {
        "semantic_similarity": 0.91,
        "skill_match": 0.85,
        "career_growth": 0.80,
        "activity": 0.75,
        "experience_fit": 0.90
      },
      "explanation": "Strong match — 4+ years Python, expert in FastAPI and LangChain...",
      "metadata": { "email": "...", "location": "...", "skills": [...] }
    }
  ],
  "parsed_jd": { "job_title": "...", "required_skills": [...] },
  "processing_time_sec": 2.3,
  "total_candidates_evaluated": 50
}
```

### `GET /health`

```json
{
  "status": "ok",
  "candidates_indexed": 50,
  "llm_available": true,
  "version": "1.0.0"
}
```

---

## 🎨 UI Features

| Feature | Description |
|---------|-------------|
| **Cinematic Splash Screen** | Full-screen animated landing with logo zoom-out & glow effects |
| **AI Pipeline Stepper** | Visual flow: JD → Embed → Score → Explain |
| **Interactive Filters** | Real-time filter by location, match %, salary, notice period |
| **Candidate Leaderboard** | Sortable ranked table with all key metrics |
| **Side-by-Side Comparison** | Compare up to 3 candidates with full score breakdowns |
| **Detailed Profiles** | Score rings, skill match highlighting, AI recruiter notes |
| **Export** | Download results as JSON or CSV |

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

Services:
- **`api`** → FastAPI on port `8000`
- **`ui`** → Streamlit on port `8501`

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| **LLM** | Groq Llama-3.3-70B-Versatile |
| **Embeddings** | Sentence Transformers (all-MiniLM-L6-v2) |
| **Vector DB** | ChromaDB (in-process, persistent) |
| **Agentic Pipeline** | LangGraph |
| **Backend API** | FastAPI + Uvicorn |
| **Frontend** | Streamlit (custom CSS, glassmorphism) |
| **Deployment** | Docker + Docker Compose |

---

## 👨‍💻 Author

**Vinay Babannavar**  
T. John Institute of Technology, Bengaluru  
Redrob AI Hackathon 2026

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
