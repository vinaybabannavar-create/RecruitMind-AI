<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=RecruitMind%20AI&fontSize=80&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Next-Generation%20Agentic%20Talent%20Discovery%20Platform&descAlignY=60&descSize=18" width="100%"/>

<br/>

<a href="https://github.com/vinaybabannavar-create/RecruitMind-AI/stargazers">
  <img src="https://img.shields.io/github/stars/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=starship&color=f5a623&labelColor=1a1a2e" alt="Stars"/>
</a>
<a href="https://github.com/vinaybabannavar-create/RecruitMind-AI/network/members">
  <img src="https://img.shields.io/github/forks/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=git&color=7c3aed&labelColor=1a1a2e" alt="Forks"/>
</a>
<img src="https://img.shields.io/badge/Redrob_AI-Hackathon_2026-FF4B4B?style=for-the-badge&logo=rocket&logoColor=white&labelColor=1a1a2e" alt="Hackathon"/>
<img src="https://img.shields.io/badge/Status-Submission_Ready-22C55E?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=1a1a2e" alt="Status"/>

<br/><br/>

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.39-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/LangGraph-Agentic_Pipeline-6C63FF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/ChromaDB-Vector_Search-F97316?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Groq-Llama--3.3--70B-22C55E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>

<br/><br/>

> 🧠 **RecruitMind AI** — Where AI meets hiring intelligence. Paste a JD, get a ranked, explained shortlist in seconds.

<br/>

**[🚀 Overview](#-overview) · [🏗️ Architecture](#-system-architecture) · [🧠 Pipeline](#-langgraph-agentic-pipeline) · [🔬 Scoring](#-multi-signal-scoring-engine) · [⚙️ Setup](#-setup--installation) · [📡 API](#-api-reference) · [🎨 UI](#-ui-features) · [🐳 Docker](#-docker-deployment)**

</div>

---

## 🎥 Demo

<div align="center">

> **Watch the full demo — JD input → AI ranking → explainable shortlist in under 3 seconds**

[![Watch Demo](https://img.shields.io/badge/▶_Watch-Full_Demo_Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/vinaybabannavar-create/RecruitMind-AI)
[![Live API Docs](https://img.shields.io/badge/📡_Explore-API_Docs-009688?style=for-the-badge&logo=fastapi&logoColor=white)](http://localhost:8000/docs)

</div>

---

## 🚀 Overview

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════╗
║  Paste a Job Description  →  RecruitMind AI thinks like a recruiter  ║
║           →  Ranked shortlist with AI explanations in seconds        ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

**RecruitMind AI** is a fully agentic, production-ready AI recruitment intelligence platform built on a **6-node LangGraph stateful pipeline**. It moves far beyond keyword filtering — using semantic vector search, LLM-powered cognitive JD parsing, multi-signal composite scoring, and explainable AI reasoning to surface the *exact right candidates* for any job description.

<div align="center">

| ❌ Traditional ATS | ✅ RecruitMind AI |
|:------------------:|:-----------------:|
| Keyword matching | Semantic intent understanding |
| Pass / Fail filter | 5-signal composite scoring |
| No explanation | Per-candidate AI recruiter notes |
| Homogeneous results | Diversity-aware re-ranking |
| Black box | Full transparent score breakdown |

</div>

### ✨ Key Highlights

<table>
<tr>
<td width="50%">

🔍 **Cognitive JD Parsing**
LLM extracts skills, seniority, culture signals, and *implicit* requirements from raw JD text

📊 **Multi-Signal Scoring Engine**
Composite scores across 5 independent signals — not just keyword overlap

💡 **Explainable AI Shortlists**
Natural language recruiter notes per candidate via Groq Llama-3.3-70B

🎯 **Semantic Vector Search**
ChromaDB + Sentence Transformers for deep contextual matching

</td>
<td width="50%">

⚡ **LangGraph Agentic Pipeline**
Modular, observable, stateful 6-node pipeline with typed state

🔁 **Diversity Re-ranking**
Prevents shortlist homogeneity — balances seniority and role types

🌐 **Offline Fallback Mode**
Works fully without any LLM API key using rule-based parsing

🐳 **One-Command Docker Deploy**
Full stack up in seconds with docker-compose

</td>
</tr>
</table>

---

## 🏗️ System Architecture

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          ✦  INPUT LAYER  ✦                              │
│                                                                         │
│    📄 Job Description Text    👤 Candidate Profiles    📡 Signals       │
└────────────┬──────────────────────────┬──────────────────┬─────────────┘
             │                          │                  │
             ▼                          ▼                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        ✦  PROCESSING LAYER  ✦                           │
│                                                                         │
│   🤖 LLM JD Parser          🔢 Embedding Engine      📊 Signal Extract  │
│   (Groq / Offline)          (sentence-transformers)   (GitHub + Rules)  │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ✦  ORCHESTRATION — LangGraph  ✦                      │
│                                                                         │
│    parse_jd → embed_jd → retrieve → score → rerank → explain           │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
     🗃️ ChromaDB             📋 Metadata            ⚡ Cache
    Vector Store             SQLite / Mongo         (Redis opt.)
              └────────────────────┼────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         ✦  OUTPUT LAYER  ✦                              │
│                                                                         │
│   FastAPI REST API  →  Streamlit Dashboard  →  Export (JSON / CSV)     │
└─────────────────────────────────────────────────────────────────────────┘
```

</div>

### 📁 Project Structure

```
RecruitMind-AI/
│
├── 📂 api/
│   ├── main.py              # FastAPI: /health /rank /explain /index /candidates
│   └── __init__.py
│
├── 📂 pipeline/
│   ├── jd_parser.py         # LLM + offline JD structured extraction
│   ├── embedder.py          # Sentence Transformers + ChromaDB engine
│   ├── scorer.py            # 5-signal composite scoring functions
│   ├── ranker.py            # LangGraph 6-node state graph (brain of system)
│   ├── explainer.py         # LLM + rule-based recruiter note generator
│   └── __init__.py
│
├── 📂 data/
│   ├── generate_candidates.py   # 100 synthetic profile generator
│   └── candidates.json          # Pre-generated dataset (ready to use)
│
├── 📂 ui/
│   └── app.py               # Streamlit premium recruiter dashboard
│
├── 📂 .github/workflows/
│   └── ci.yml               # GitHub Actions CI pipeline
│
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container build config
├── docker-compose.yml       # Multi-service orchestration
├── run.sh                   # One-command startup script
├── LICENSE                  # MIT License
└── README.md
```

---

## 🧠 LangGraph Agentic Pipeline

<div align="center">

The entire ranking process is a **LangGraph stateful graph** — each stage is an independent, testable node operating on a shared typed `RankingState`.

</div>

```
                         ┌──────────────────┐
                         │    📄 JD Input    │
                         └────────┬─────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    Node 1: parse_jd         │
                    │  🤖 LLM extracts:           │
                    │  • Required & nice skills   │
                    │  • Seniority level          │
                    │  • Culture signals          │
                    │  • Implicit expectations    │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    Node 2: embed_jd         │
                    │  🔢 Sentence Transformer    │
                    │  converts JD → dense vector │
                    │  (all-MiniLM-L6-v2)         │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    Node 3: retrieve         │
                    │  🗃️ ChromaDB cosine search  │
                    │  returns top-N semantically │
                    │  similar candidates         │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    Node 4: score            │
                    │  📊 5-signal composite:     │
                    │  semantic + skill + career  │
                    │  + activity + exp fit       │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    Node 5: rerank           │
                    │  🔁 Diversity-aware sort    │
                    │  Prevents seniority &       │
                    │  role-type homogeneity      │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    Node 6: explain          │
                    │  💬 Groq Llama-3.3-70B      │
                    │  writes recruiter-style     │
                    │  reasoning per candidate    │
                    └─────────────┬──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │    ✅ Ranked Shortlist       │
                    │  rank · score · breakdown   │
                    │  explanation · metadata     │
                    └────────────────────────────┘
```

**State is fully typed** using Python `TypedDict` — every node receives and emits the complete `RankingState`, making each stage independently testable, inspectable, and extensible.

---

## 🔬 Multi-Signal Scoring Engine

<div align="center">

RecruitMind AI never ranks on a single dimension. Every candidate gets a **composite score from 5 independent signals**, each measuring a different aspect of job fit.

</div>

<div align="center">

| Signal | Weight | How It's Computed |
|:------:|:------:|:-----------------:|
| 🧬 **Semantic Similarity** | **35%** | Cosine distance between JD embedding and candidate profile embedding via ChromaDB |
| 🛠️ **Skill Match** | **30%** | Required skills hit rate (80%) + nice-to-have bonus (20%) |
| 📈 **Career Growth** | **15%** | Raw growth score × tenure stability × promotions count |
| ⚡ **Activity Signal** | **10%** | GitHub contributions + open source PRs + LeetCode + hackathons × recency multiplier |
| 📅 **Experience Fit** | **10%** | Linear fit to JD experience range + seniority alignment penalty |

</div>

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   Score = (0.35 × Semantic) + (0.30 × Skill) + (0.15 × Career) ║
║                + (0.10 × Activity) + (0.10 × ExperienceFit)     ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

> Scores pass through the **diversity re-ranker** which applies a mild penalty to over-represented seniority levels or role types — ensuring balanced, varied shortlists.

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.11+  
- pip  
- Git  
- Groq API key — **free** at [console.groq.com](https://console.groq.com) *(fully optional — works without it)*

---

### ⚡ Option A — One-Command Startup (Recommended)

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
bash run.sh
```

That's it. `run.sh` handles everything: venv check, dependency install, env setup, candidate generation, API start, and Streamlit launch.

---

### 🔧 Option B — Manual Step-by-Step

**Step 1 — Clone**
```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
```

**Step 2 — Virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```
> `sentence-transformers` downloads `all-MiniLM-L6-v2` (~80MB) on first run automatically.

**Step 4 — Configure environment**
```bash
cp .env.example .env
# Edit .env — add your GROQ_API_KEY (optional)
```

```env
GROQ_API_KEY=your_groq_api_key_here
API_URL=http://localhost:8000
```

**Step 5 — Generate candidates**
```bash
python data/generate_candidates.py
```

**Step 6 — Index into ChromaDB**
```bash
python -c "from pipeline.embedder import get_engine; get_engine().index_candidates()"
```

**Step 7 — Start API (Terminal 1)**
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

**Step 8 — Start Dashboard (Terminal 2)**
```bash
streamlit run ui/app.py --server.port 8501
```

Open → **http://localhost:8501** 🎉

---

## 📡 API Reference

<div align="center">

| Method | Endpoint | Description |
|:------:|:--------:|:-----------:|
| `POST` | `/rank` | Full pipeline — JD in, ranked shortlist out |
| `GET` | `/health` | System health + indexing status |
| `GET` | `/candidates` | Paginated candidate list |
| `GET` | `/candidate/{id}` | Single candidate profile |
| `POST` | `/index` | Re-index candidates (background) |
| `POST` | `/explain` | Add AI explanations to shortlist |

</div>

### `POST /rank` — Main Endpoint

**Request:**
```json
{
  "jd_text": "Senior Python ML Engineer, 4+ years, FastAPI, LangChain, Docker, RAG pipelines, Bengaluru",
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
      "candidate_id": "CAND_0042",
      "name": "Aditya Sharma",
      "composite_score": 0.87,
      "score_breakdown": {
        "semantic_similarity": 0.91,
        "skill_match": 0.85,
        "career_growth": 0.80,
        "activity": 0.75,
        "experience_fit": 0.90
      },
      "explanation": "Ranked #1 — strong match on Python, FastAPI, and LangChain (85% skill overlap). 5 years senior-level experience aligns perfectly. Active open source contributor with 14 PRs. Minor gap: no AWS certification.",
      "metadata": {
        "email": "aditya.sharma@email.com",
        "location": "Bengaluru",
        "years_experience": 5,
        "seniority": "senior",
        "skills": ["Python", "FastAPI", "LangChain", "Docker", "PostgreSQL"],
        "certifications": ["AWS Solutions Architect"],
        "expected_salary_lpa": 22.5,
        "notice_period_days": 30
      }
    }
  ],
  "parsed_jd": {
    "job_title": "Senior ML Engineer",
    "required_skills": ["Python", "FastAPI", "LangChain", "Docker"],
    "seniority_level": "senior",
    "min_experience_years": 4
  },
  "total_candidates_evaluated": 20,
  "processing_time_sec": 1.8,
  "warning": null
}
```

### `GET /health`
```json
{
  "status": "ok",
  "candidates_indexed": 100,
  "vector_db_ready": true,
  "llm_available": true,
  "version": "1.0.0"
}
```

> 📖 Full interactive API docs at **http://localhost:8000/docs** (Swagger UI)

---

## 🎨 UI Features

<div align="center">

The Streamlit dashboard is built for a **recruiter who needs answers fast** — clean, visual, and intelligent.

</div>

<table>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
<tr>
<td>📋 <b>JD Input Panel</b></td>
<td>Paste any job description + 5 one-click industry quick-fill templates</td>
</tr>
<tr>
<td>🔴 <b>Live Pipeline Stepper</b></td>
<td>Real-time step progress — Parsing JD → Embedding → Searching → Scoring → Explaining</td>
</tr>
<tr>
<td>🔗 <b>Live API Status</b></td>
<td>Sidebar health check — shows indexed candidate count and LLM mode</td>
</tr>
<tr>
<td>📊 <b>Summary Metrics</b></td>
<td>Candidates ranked · Total evaluated · Processing time · Skills matched</td>
</tr>
<tr>
<td>🔍 <b>Parsed JD Expander</b></td>
<td>See exactly what the AI extracted from your JD — skills, seniority, expectations</td>
</tr>
<tr>
<td>🏆 <b>Ranked Leaderboard</b></td>
<td>Sortable table with all key metrics — score, experience, salary, notice period</td>
</tr>
<tr>
<td>📋 <b>Detailed Profile Cards</b></td>
<td>Expandable per-candidate cards with complete profile and score breakdown</td>
</tr>
<tr>
<td>💬 <b>AI Recruiter Notes</b></td>
<td>LLM-generated explanation card for every ranked candidate</td>
</tr>
<tr>
<td>🟢 <b>Skill Highlighting</b></td>
<td>Green = matched required skills · Grey = additional skills</td>
</tr>
<tr>
<td>📈 <b>Score Breakdown Bars</b></td>
<td>Visual sub-score bars for all 5 signals per candidate</td>
</tr>
<tr>
<td>📥 <b>Export</b></td>
<td>Download full results as <b>JSON</b> or clean shortlist as <b>CSV</b></td>
</tr>
</table>

---

## 🧪 Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_scorer.py -v
```

---

## 📊 Sample Output

Here is a real example of what the `/rank` endpoint returns for the query *"Senior Python ML Engineer, 4+ years, FastAPI + LangChain + Docker"*:

```json
{
  "shortlist": [
    {
      "rank": 1,
      "candidate_id": "CAND_0042",
      "name": "Aditya Sharma",
      "composite_score": 0.87,
      "score_breakdown": {
        "semantic_similarity": 0.91,
        "skill_match": 0.85,
        "career_growth": 0.80,
        "activity": 0.75,
        "experience_fit": 0.90
      },
      "explanation": "Ranked #1 — strong match on Python, FastAPI and LangChain (85% skill overlap). 5 years senior-level experience aligns perfectly with requirement. Active open source contributor (14 PRs). Minor gap: no AWS certification listed.",
      "metadata": {
        "email": "aditya.sharma@email.com",
        "location": "Bengaluru",
        "years_experience": 5,
        "seniority": "senior",
        "skills": ["Python", "FastAPI", "LangChain", "Docker", "PostgreSQL"],
        "certifications": ["AWS Solutions Architect"],
        "expected_salary_lpa": 22.5,
        "notice_period_days": 30
      }
    }
  ],
  "parsed_jd": {
    "job_title": "Senior ML Engineer",
    "required_skills": ["Python", "FastAPI", "LangChain", "Docker"],
    "seniority_level": "senior",
    "min_experience_years": 4
  },
  "total_candidates_evaluated": 20,
  "processing_time_sec": 1.8,
  "warning": null
}
```

---

## 🗺️ Roadmap

RecruitMind AI is built to grow. Here's what's planned beyond the hackathon:

- [ ] **Resume PDF parsing** — extract skills directly from uploaded resumes (PyMuPDF + LLM)
- [ ] **Real LinkedIn profile integration** via LinkedIn API for live candidate data
- [ ] **Feedback loop** — recruiter marks hired/rejected, system learns from outcomes
- [ ] **Multi-JD batch ranking** — rank 100s of candidates across multiple open roles simultaneously
- [ ] **Bias detection layer** — flag potential discrimination signals in JD language or scoring patterns
- [ ] **Production PostgreSQL + pgvector migration** from ChromaDB for horizontal scaling

---

## 🐳 Docker Deployment

> No local Python setup needed. One command brings the entire stack online.

```bash
# Clone and configure
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
cp .env.example .env
# Optionally add GROQ_API_KEY to .env

# Launch everything
docker-compose up --build
```

<div align="center">

| Service | URL | Description |
|:-------:|:---:|:-----------:|
| 🎨 Streamlit UI | http://localhost:8501 | Recruiter dashboard |
| ⚡ FastAPI Backend | http://localhost:8000 | REST API |
| 📖 API Docs | http://localhost:8000/docs | Swagger UI |

</div>

```bash
# Stop all services
docker-compose down
```

---

## 📦 Full Tech Stack

<div align="center">

| Layer | Technology | Version | Purpose |
|:-----:|:----------:|:-------:|:-------:|
| 🤖 **LLM** | Groq Llama-3.3-70B-Versatile | Latest | JD parsing + explanation generation |
| 🔢 **Embeddings** | sentence-transformers | 3.0.1 | Dense vector encoding |
| 🗃️ **Vector DB** | ChromaDB | 0.5.3 | Persistent semantic search |
| ⚡ **Orchestration** | LangGraph | 0.2.14 | Stateful agentic pipeline |
| 🌐 **Backend API** | FastAPI + Uvicorn | 0.115 | Async REST endpoints |
| 🎨 **Frontend** | Streamlit | 1.39 | Interactive recruiter dashboard |
| 🐳 **Deployment** | Docker + Compose | Latest | One-command containerization |
| 📦 **Data** | Synthetic JSON | — | 100 realistic candidate profiles |

</div>

---

## 🗂️ Candidate Data Schema

Each of the 100 synthetic candidates carries a rich, realistic profile:

```json
{
  "id": "CAND_0042",
  "name": "Aditya Sharma",
  "summary": "Senior ML engineer with 5 years experience building AI pipelines...",
  "years_experience": 5,
  "seniority": "senior",
  "role_type": "ml",
  "skills": ["Python", "FastAPI", "LangChain", "Docker", "PostgreSQL", "RAG"],
  "education": {
    "degree": "B.Tech Computer Science",
    "college": "NIT Trichy",
    "graduation_year": 2019,
    "cgpa": 8.7
  },
  "experience": [
    { "company": "Razorpay", "role": "ML Engineer", "duration_years": 3 },
    { "company": "Startup XYZ", "role": "Python Developer", "duration_years": 2 }
  ],
  "certifications": ["AWS Solutions Architect", "TensorFlow Developer Certificate"],
  "github": {
    "repos": 24,
    "contributions_last_year": 380,
    "open_source_prs": 14,
    "github_score": 0.82
  },
  "activity_signals": {
    "leetcode_solved": 210,
    "hackathon_participations": 4,
    "blog_posts": 6,
    "last_active_days_ago": 12
  },
  "career_signals": {
    "career_growth_score": 0.82,
    "promotions": 2,
    "avg_tenure_years": 2.5
  },
  "expected_salary_lpa": 22.5,
  "notice_period_days": 30,
  "location": "Bengaluru",
  "open_to_remote": true
}
```

---

## 💡 RecruitMind AI vs. The World

<div align="center">

```
┌──────────────────────┬─────────────────────┬──────────────────────────────────────┐
│      Dimension       │   Traditional ATS   │          RecruitMind AI              │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  JD Understanding    │  Keyword extraction  │  LLM semantic parsing + implicit     │
│                      │                     │  requirement detection               │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Matching            │  if skill in resume  │  Cosine similarity over dense        │
│                      │                     │  vector embeddings                   │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Scoring             │  Binary pass/fail    │  5-signal weighted composite score   │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Ranking             │  Date applied        │  Multi-dimensional AI score          │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Explanation         │  None                │  Per-candidate LLM recruiter note    │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Diversity           │  None                │  Built-in diversity re-ranker        │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Transparency        │  Black box           │  Full score breakdown per signal     │
├──────────────────────┼─────────────────────┼──────────────────────────────────────┤
│  Offline Support     │  N/A                 │  Rule-based fallback — always works  │
└──────────────────────┴─────────────────────┴──────────────────────────────────────┘
```

</div>

---

## 📁 Key Files Reference

<div align="center">

| File | Role |
|:----:|:----:|
| `pipeline/ranker.py` | 🧠 LangGraph graph — the core brain of the system |
| `pipeline/scorer.py` | 📊 All 5 scoring functions + composite calculator |
| `pipeline/jd_parser.py` | 🤖 LLM + offline JD structured extraction |
| `pipeline/embedder.py` | 🔢 ChromaDB indexing + semantic search |
| `pipeline/explainer.py` | 💬 LLM + rule-based explanation generator |
| `api/main.py` | ⚡ FastAPI with 6 REST endpoints |
| `ui/app.py` | 🎨 Full Streamlit recruiter dashboard |
| `data/generate_candidates.py` | 👥 Synthetic 100-candidate dataset generator |
| `run.sh` | 🚀 One-command startup script |
| `docker-compose.yml` | 🐳 Full stack Docker orchestration |

</div>

---

## 🔑 Getting a Free Groq API Key

```
1. Visit  →  https://console.groq.com
2. Sign up (free — no credit card required)
3. Go to  →  API Keys → Create API Key
4. Copy key → paste into .env as GROQ_API_KEY=your_key
```

> **No key?** No problem. RecruitMind AI automatically falls back to rule-based offline mode for JD parsing and explanations. All semantic search and scoring still works fully — you won't lose core functionality.

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request
```

---

## 👨‍💻 Author

<div align="center">

<br/>

**Vinay Babannavar**

*B.E. Computer Science Engineering*
*T. John Institute of Technology, Bengaluru | CGPA: 8.7 | Expected Graduation: 2027*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-vinaybabannavar--create-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vinaybabannavar-create)

<br/>

![Azure AI-900](https://img.shields.io/badge/Microsoft-AI--900-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![Azure AZ-900](https://img.shields.io/badge/Microsoft-AZ--900-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-Certified-1BA0D7?style=flat-square&logo=cisco&logoColor=white)
![NPTEL](https://img.shields.io/badge/NPTEL-Python-FF6B35?style=flat-square)

<br/>

*Redrob AI Hackathon 2026 — Data & AI Challenge: Intelligent Candidate Discovery*

<br/>

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Built with ❤️ using LangGraph · ChromaDB · Groq · FastAPI · Streamlit**

*RecruitMind AI — Because great candidates deserve to be found.*

⭐ **If this project helped you, please give it a star!** ⭐

</div>
