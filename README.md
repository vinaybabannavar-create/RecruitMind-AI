<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=RecruitMind%20AI&fontSize=90&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Next-Generation%20Agentic%20Talent%20Discovery%20Platform&descAlignY=62&descSize=20" width="100%"/>

<br/>

[![Stars](https://img.shields.io/github/stars/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=starship&color=f5a623&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/stargazers)
[![Forks](https://img.shields.io/github/forks/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=git&color=7c3aed&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/network/members)
[![CI](https://img.shields.io/github/actions/workflow/status/vinaybabannavar-create/RecruitMind-AI/ci.yml?style=for-the-badge&label=CI&logo=githubactions&logoColor=white&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/actions)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&labelColor=1a1a2e)](LICENSE)
[![Hackathon](https://img.shields.io/badge/Redrob_AI-Hackathon_2026-FF4B4B?style=for-the-badge&logo=rocket&logoColor=white&labelColor=1a1a2e)](https://hack2skill.com)
[![Status](https://img.shields.io/badge/Status-Submitted_✓-22C55E?style=for-the-badge&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI)

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_Pipeline-6C63FF?style=for-the-badge)](https://langchain-ai.github.io/langgraph)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Search-F97316?style=for-the-badge)](https://www.trychroma.com)
[![Groq](https://img.shields.io/badge/Groq-Llama--3.3--70B-22C55E?style=for-the-badge)](https://groq.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

<br/><br/>

<h3>🧠 Where AI meets hiring intelligence.</h3>
<h4>Paste a Job Description → Get a ranked, explained shortlist in seconds.</h4>

<br/>

**[🚀 Overview](#-overview) · [🎥 Demo](#-demo) · [🏗️ Architecture](#-system-architecture) · [🧠 Pipeline](#-langgraph-agentic-pipeline) · [🔬 Scoring](#-multi-signal-scoring-engine) · [⚙️ Setup](#-setup--installation) · [📡 API](#-api-reference) · [🐳 Docker](#-docker-deployment)**

</div>

---

## 🎥 Demo

<div align="center">

> **Watch the full demo — JD input → AI ranking → explainable shortlist in under 3 seconds**

[![Watch Demo](https://img.shields.io/badge/▶_Watch-Full_Demo_Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/vinaybabannavar-create/RecruitMind-AI)
[![API Docs](https://img.shields.io/badge/📡_Explore-Live_API_Docs-009688?style=for-the-badge&logo=fastapi&logoColor=white)](http://localhost:8000/docs)
[![GitHub](https://img.shields.io/badge/⭐_Star-This_Repo-f5a623?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vinaybabannavar-create/RecruitMind-AI)

</div>

---

## 🚀 Overview

**RecruitMind AI** is a fully agentic, production-ready AI recruitment intelligence platform built on a **6-node LangGraph stateful pipeline**. It moves far beyond keyword filtering — using semantic vector search, LLM-powered cognitive JD parsing, multi-signal composite scoring, and explainable AI reasoning to surface the *exact right candidates* for any job description.

<div align="center">

<br/>

> **Traditional ATS filters by keywords. RecruitMind AI understands intent.**

<br/>

<table>
<thead>
<tr>
<th>❌ Traditional ATS</th>
<th>✅ RecruitMind AI</th>
</tr>
</thead>
<tbody>
<tr>
<td>Keyword matching only</td>
<td>🧠 Semantic intent understanding via LLM</td>
</tr>
<tr>
<td>Binary pass / fail filter</td>
<td>📊 5-signal weighted composite scoring</td>
</tr>
<tr>
<td>No explanation given</td>
<td>💬 Per-candidate AI recruiter notes</td>
</tr>
<tr>
<td>Homogeneous results</td>
<td>🔁 Diversity-aware re-ranking</td>
</tr>
<tr>
<td>Complete black box</td>
<td>🔍 Full transparent score breakdown</td>
</tr>
<tr>
<td>Fails without data</td>
<td>🌐 Rule-based offline fallback mode</td>
</tr>
</tbody>
</table>

</div>

<br/>

### ✨ Key Highlights

<table>
<tr>
<td width="50%" valign="top">

**🔍 Cognitive JD Parsing**<br/>
LLM extracts skills, seniority, culture signals, and *implicit* requirements from raw JD text — not just keywords

**📊 Multi-Signal Scoring Engine**<br/>
Composite scores across 5 independent signals — semantic fit, skill match, career growth, activity, experience

**💡 Explainable AI Shortlists**<br/>
Every candidate gets a natural language recruiter note generated by Groq Llama-3.3-70B — grounded in real data

**🎯 Semantic Vector Search**<br/>
ChromaDB + Sentence Transformers (all-MiniLM-L6-v2) for deep contextual matching beyond surface keywords

</td>
<td width="50%" valign="top">

**⚡ LangGraph Agentic Pipeline**<br/>
Modular, observable, stateful 6-node pipeline with fully typed `RankingState` — each node independently testable

**🔁 Diversity Re-ranking**<br/>
Prevents shortlist homogeneity — applies diversity multiplier across seniority levels and role types

**🌐 Offline Fallback Mode**<br/>
Works fully without any LLM API key using deterministic rule-based parsing — zero dependency failure

**🐳 One-Command Docker Deploy**<br/>
Full stack (API + UI) up in seconds with a single `docker-compose up --build`

</td>
</tr>
</table>

---

## 🏗️ System Architecture

<div align="center">

<table>
<tr>
<td align="center" width="100%">

### INPUT LAYER

</td>
</tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center" width="33%" style="background:#1a1a2e;color:white;padding:12px;border-radius:8px">

**📄 Job Description**<br/>
<sub>Text / PDF / URL</sub>

</td>
<td align="center" width="5%">·</td>
<td align="center" width="33%" style="background:#1a1a2e;color:white;padding:12px;border-radius:8px">

**👤 Candidate Profiles**<br/>
<sub>100 rich JSON profiles</sub>

</td>
<td align="center" width="5%">·</td>
<td align="center" width="33%" style="background:#1a1a2e;color:white;padding:12px;border-radius:8px">

**📡 Behavioral Signals**<br/>
<sub>GitHub · LeetCode · Activity</sub>

</td>
</tr>
</table>
</td>
</tr>
<tr><td align="center">⬇️ ⬇️ ⬇️</td></tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center">

### PROCESSING LAYER

</td>
</tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center" width="33%" style="background:#4c1d95;color:white;padding:12px;border-radius:8px">

**🤖 LLM JD Parser**<br/>
<sub>Groq Llama-3.3 / Offline fallback</sub>

</td>
<td align="center" width="5%">→</td>
<td align="center" width="33%" style="background:#4c1d95;color:white;padding:12px;border-radius:8px">

**🔢 Embedding Engine**<br/>
<sub>sentence-transformers<br/>all-MiniLM-L6-v2</sub>

</td>
<td align="center" width="5%">→</td>
<td align="center" width="33%" style="background:#4c1d95;color:white;padding:12px;border-radius:8px">

**📊 Signal Extractor**<br/>
<sub>GitHub API + heuristics</sub>

</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#6c63ff;color:white;padding:16px;border-radius:8px">

### ⚡ ORCHESTRATION — LangGraph Pipeline

**`parse_jd` → `embed_jd` → `retrieve` → `score` → `rerank` → `explain`**

<sub>Fully typed RankingState · Each node independently testable · Stateful graph execution</sub>

</td>
</tr>
<tr><td align="center">⬇️ ⬇️ ⬇️</td></tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center">

### STORAGE LAYER

</td>
</tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center" width="33%" style="background:#065f46;color:white;padding:12px;border-radius:8px">

**🗃️ ChromaDB**<br/>
<sub>Vector store · Cosine similarity · Persistent</sub>

</td>
<td align="center" width="5%">·</td>
<td align="center" width="33%" style="background:#065f46;color:white;padding:12px;border-radius:8px">

**📋 Metadata Store**<br/>
<sub>candidates.json · Profile data</sub>

</td>
<td align="center" width="5%">·</td>
<td align="center" width="33%" style="background:#065f46;color:white;padding:12px;border-radius:8px">

**⚡ Cache (Optional)**<br/>
<sub>Redis · Fast repeat queries</sub>

</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center">

### OUTPUT LAYER

</td>
</tr>
<tr>
<td>
<table width="100%">
<tr>
<td align="center" width="33%" style="background:#7c2d12;color:white;padding:12px;border-radius:8px">

**🌐 FastAPI REST API**<br/>
<sub>6 endpoints · Swagger docs</sub>

</td>
<td align="center" width="5%">→</td>
<td align="center" width="33%" style="background:#7c2d12;color:white;padding:12px;border-radius:8px">

**🎨 Streamlit Dashboard**<br/>
<sub>Ranked cards · Score bars · AI notes</sub>

</td>
<td align="center" width="5%">→</td>
<td align="center" width="33%" style="background:#7c2d12;color:white;padding:12px;border-radius:8px">

**📥 Export**<br/>
<sub>JSON · CSV · Download</sub>

</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>

</div>

<br/>

### 📁 Project Structure

```
RecruitMind-AI/
│
├── 📂 api/
│   ├── main.py                  # FastAPI — /health /rank /explain /index /candidates /candidate/{id}
│   └── __init__.py
│
├── 📂 pipeline/
│   ├── jd_parser.py             # LLM + offline JD structured extraction
│   ├── embedder.py              # Sentence Transformers + ChromaDB indexing & search
│   ├── scorer.py                # 5-signal composite scoring functions
│   ├── ranker.py                # LangGraph 6-node state graph — brain of system
│   ├── explainer.py             # Groq LLM + rule-based recruiter note generator
│   └── __init__.py
│
├── 📂 data/
│   ├── generate_candidates.py   # 100 synthetic profile generator
│   └── candidates.json          # Pre-generated dataset (ready to use)
│
├── 📂 ui/
│   └── app.py                   # Streamlit premium recruiter dashboard
│
├── 📂 .github/workflows/
│   └── ci.yml                   # GitHub Actions CI — automated tests on every push
│
├── .env.example                 # Environment variables template
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.sh                       # One-command startup script
├── LICENSE
└── README.md
```

---

## 🧠 LangGraph Agentic Pipeline

<div align="center">

The entire ranking process runs as a **LangGraph stateful graph** — each stage is an independent, testable node operating on a shared typed `RankingState`.

<br/>

<table>
<tr>
<td align="center" colspan="3">

```
📄 JD INPUT
```

</td>
</tr>
<tr>
<td align="center">⬇️</td>
</tr>
</table>

<table width="80%">
<tr>
<td align="center" style="background:#1e1b4b;color:white;padding:16px;border-radius:10px;border-left:4px solid #6c63ff">

### 🟣 Node 1 — `parse_jd`
**Groq Llama-3.3-70B** (or offline fallback)<br/><br/>
Extracts → Job Title · Required Skills · Nice-to-Have Skills<br/>
Seniority Level · Culture Signals · Implicit Expectations<br/>
<sub>Output: Structured JSON dict</sub>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#1e3a5f;color:white;padding:16px;border-radius:10px;border-left:4px solid #0ea5e9">

### 🔵 Node 2 — `embed_jd`
**sentence-transformers** (all-MiniLM-L6-v2)<br/><br/>
Converts JD text → 384-dimensional dense vector<br/>
CPU-only · ~80MB model · No GPU required<br/>
<sub>Output: Float vector [384]</sub>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#1a3a2a;color:white;padding:16px;border-radius:10px;border-left:4px solid #22c55e">

### 🟢 Node 3 — `retrieve`
**ChromaDB** cosine similarity search<br/><br/>
Searches 100 indexed candidate embeddings<br/>
Returns top-20 most semantically similar profiles<br/>
<sub>Output: Candidates with semantic_score per profile</sub>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#3a1a00;color:white;padding:16px;border-radius:10px;border-left:4px solid #f97316">

### 🟠 Node 4 — `score`
**Multi-Signal Composite Scoring**<br/><br/>
Signal 1: Semantic similarity (35%) · Signal 2: Skill match (30%)<br/>
Signal 3: Career growth (15%) · Signal 4: Activity (10%) · Signal 5: Exp fit (10%)<br/>
<sub>Output: Composite score 0.0–1.0 per candidate</sub>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#3a1a3a;color:white;padding:16px;border-radius:10px;border-left:4px solid #a855f7">

### 🟡 Node 5 — `rerank`
**Diversity-Aware Re-ranking**<br/><br/>
Applies 0.95× penalty to over-represented seniority/role types<br/>
Ensures balanced shortlist — not 10 identical senior ML engineers<br/>
<sub>Output: Reranked sorted list with rank numbers assigned</sub>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#1a3a2a;color:white;padding:16px;border-radius:10px;border-left:4px solid #10b981">

### 💬 Node 6 — `explain`
**Groq Llama-3.3-70B** (or rule-based fallback)<br/><br/>
Generates 3-4 sentence recruiter-style note per candidate<br/>
Grounded strictly in candidate data — zero hallucination<br/>
<sub>Output: Final ranked shortlist with explanations</sub>

</td>
</tr>
<tr><td align="center">⬇️</td></tr>
<tr>
<td align="center" style="background:#0f0f1a;color:white;padding:16px;border-radius:10px;border:2px solid #6c63ff">

### ✅ RANKED SHORTLIST OUTPUT
`rank` · `composite_score` · `score_breakdown` (5 signals) · `explanation` · `metadata`

</td>
</tr>
</table>

</div>

> **State is fully typed** using Python `TypedDict` — every node receives and emits the complete `RankingState`, making each stage independently testable, inspectable, and extensible without touching other nodes.

---

## 🔬 Multi-Signal Scoring Engine

<div align="center">

Every candidate receives a **composite score built from 5 independent signals** — each measuring a completely different dimension of fit.

<br/>

<table>
<thead>
<tr>
<th>Signal</th>
<th>Weight</th>
<th>Algorithm</th>
<th>Range</th>
</tr>
</thead>
<tbody>
<tr>
<td>🧬 <b>Semantic Similarity</b></td>
<td><b>35%</b></td>
<td>Cosine distance between JD embedding and candidate profile embedding via ChromaDB</td>
<td>0.0 – 1.0</td>
</tr>
<tr>
<td>🛠️ <b>Skill Match</b></td>
<td><b>30%</b></td>
<td>Required skills hit rate × 0.8 + nice-to-have bonus × 0.2</td>
<td>0.0 – 1.0</td>
</tr>
<tr>
<td>📈 <b>Career Growth</b></td>
<td><b>15%</b></td>
<td>Raw growth score × 0.6 + tenure stability × 0.3 + promotions bonus</td>
<td>0.0 – 1.0</td>
</tr>
<tr>
<td>⚡ <b>Activity Signal</b></td>
<td><b>10%</b></td>
<td>GitHub score × 0.5 + LeetCode × 0.3 + hackathons × 0.2 × recency multiplier</td>
<td>0.0 – 1.0</td>
</tr>
<tr>
<td>📅 <b>Experience Fit</b></td>
<td><b>10%</b></td>
<td>Linear penalty for under/over-experience × seniority alignment multiplier</td>
<td>0.0 – 1.0</td>
</tr>
</tbody>
</table>

<br/>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   Composite = (0.35 × Semantic) + (0.30 × Skill) + (0.15 × Career)         ║
║                      + (0.10 × Activity) + (0.10 × ExperienceFit)           ║
║                                                                              ║
║   → Diversity Re-ranker (0.95× penalty for over-represented types)          ║
║   → Sort descending → Top-K shortlist with AI explanation                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## ⚙️ Setup & Installation

### Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | 3.11+ | Required |
| pip | Latest | Required |
| Git | Any | Required |
| Groq API Key | — | **Optional** — system works without it |

---

### ⚡ Option A — One-Command Startup (Recommended)

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
bash run.sh
```

> `run.sh` handles everything automatically: dependency install → env setup → candidate generation → ChromaDB indexing → API start → Streamlit launch.

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
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```
> `sentence-transformers` downloads `all-MiniLM-L6-v2` (~80MB) on first run automatically.

**Step 4 — Configure environment**
```bash
cp .env.example .env
# Add GROQ_API_KEY=your_key (free at console.groq.com) — optional
```

**Step 5 — Generate + Index candidates**
```bash
python data/generate_candidates.py
python -c "from pipeline.embedder import get_engine; get_engine().index_candidates()"
```

**Step 6 — Start (two terminals)**
```bash
# Terminal 1
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2
streamlit run ui/app.py --server.port 8501
```

Open **http://localhost:8501** 🎉

---

## 📡 API Reference

<div align="center">

| Method | Endpoint | Description |
|:------:|:--------:|:-----------:|
| `POST` | `/rank` | Full pipeline — JD in, ranked shortlist out |
| `GET` | `/health` | System health + indexing status |
| `GET` | `/candidates` | Paginated candidate list |
| `GET` | `/candidate/{id}` | Single candidate profile by ID |
| `POST` | `/index` | Re-index candidates into ChromaDB |
| `POST` | `/explain` | Add AI explanations to an existing shortlist |

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
      "explanation": "Ranked #1 — strong match on Python, FastAPI and LangChain (85% skill overlap). 5 years senior experience aligns perfectly. Active open source contributor with 14 PRs. Minor gap: no AWS certification.",
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

> 📖 Full interactive Swagger docs at **http://localhost:8000/docs**

---

## 🎨 UI Features

<div align="center">

<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>📋 <b>JD Input Panel</b></td>
<td>Paste any job description + 5 one-click industry quick-fill templates</td>
</tr>
<tr>
<td>🔄 <b>Live Pipeline Stepper</b></td>
<td>Real-time step progress — Parsing JD → Embedding → Searching → Scoring → Explaining</td>
</tr>
<tr>
<td>🔗 <b>Live API Status</b></td>
<td>Sidebar health check — shows indexed candidate count, LLM availability mode</td>
</tr>
<tr>
<td>📊 <b>Summary Metrics</b></td>
<td>Candidates ranked · Total evaluated · Processing time · Skills matched count</td>
</tr>
<tr>
<td>🔍 <b>Parsed JD Expander</b></td>
<td>See exactly what the AI extracted from your JD — skills, seniority, implicit expectations</td>
</tr>
<tr>
<td>🏆 <b>Ranked Leaderboard</b></td>
<td>Sortable table with all key metrics — composite score, experience, salary, notice period</td>
</tr>
<tr>
<td>📋 <b>Detailed Profile Cards</b></td>
<td>Expandable per-candidate view with complete profile, certs, GitHub, LeetCode data</td>
</tr>
<tr>
<td>💬 <b>AI Recruiter Notes</b></td>
<td>LLM-generated explanation card for every ranked candidate — grounded, not hallucinated</td>
</tr>
<tr>
<td>🟢 <b>Skill Match Highlighting</b></td>
<td>Green tags = matched required skills · Grey tags = additional skills candidate has</td>
</tr>
<tr>
<td>📈 <b>Score Breakdown Bars</b></td>
<td>Visual sub-score bars for all 5 signals per candidate with color coding</td>
</tr>
<tr>
<td>📥 <b>Export</b></td>
<td>Download full results as <b>JSON</b> or clean ranked shortlist as <b>CSV</b></td>
</tr>
</tbody>
</table>

</div>

---

## 🧪 Running Tests

```bash
pip install -r requirements.txt
pytest tests/ -v
pytest tests/test_scorer.py -v   # scorer only
```

---

## 🐳 Docker Deployment

> No local Python setup needed. One command brings the full stack online.

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
cp .env.example .env             # Add GROQ_API_KEY (optional)
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
docker-compose down   # Stop all services
```

---

## 📦 Full Tech Stack

<div align="center">

<table>
<thead>
<tr>
<th>Layer</th>
<th>Technology</th>
<th>Version</th>
<th>Why Selected</th>
</tr>
</thead>
<tbody>
<tr>
<td>🤖 <b>LLM</b></td>
<td>Groq Llama-3.3-70B-Versatile</td>
<td>Latest</td>
<td>Free tier, fastest open-weight inference, excellent instruction following</td>
</tr>
<tr>
<td>🔢 <b>Embeddings</b></td>
<td>sentence-transformers</td>
<td>3.0.1</td>
<td>CPU-only, 80MB, high-quality 384-dim vectors, no API cost</td>
</tr>
<tr>
<td>🗃️ <b>Vector DB</b></td>
<td>ChromaDB (persistent)</td>
<td>0.5.3</td>
<td>In-process, no external server, cosine similarity built-in</td>
</tr>
<tr>
<td>⚡ <b>Orchestration</b></td>
<td>LangGraph</td>
<td>0.2.14</td>
<td>Stateful typed pipeline, each node independently testable</td>
</tr>
<tr>
<td>🌐 <b>Backend API</b></td>
<td>FastAPI + Uvicorn</td>
<td>0.115</td>
<td>Async Python REST, auto Swagger docs, Pydantic validation</td>
</tr>
<tr>
<td>🎨 <b>Frontend</b></td>
<td>Streamlit</td>
<td>1.39</td>
<td>Rapid recruiter dashboard with minimal frontend code</td>
</tr>
<tr>
<td>🐳 <b>Deployment</b></td>
<td>Docker + Compose</td>
<td>Latest</td>
<td>Single-command reproducible full-stack deployment</td>
</tr>
<tr>
<td>🔄 <b>CI/CD</b></td>
<td>GitHub Actions</td>
<td>—</td>
<td>Automated tests on every push — verifies logic, structure, dataset</td>
</tr>
</tbody>
</table>

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
  "education": { "degree": "B.Tech CS", "college": "NIT Trichy", "cgpa": 8.7 },
  "experience": [
    { "company": "Razorpay", "role": "ML Engineer", "duration_years": 3 }
  ],
  "certifications": ["AWS Solutions Architect", "TensorFlow Developer Certificate"],
  "github": { "repos": 24, "contributions_last_year": 380, "open_source_prs": 14 },
  "activity_signals": { "leetcode_solved": 210, "hackathon_participations": 4 },
  "career_signals": { "career_growth_score": 0.82, "promotions": 2, "avg_tenure_years": 2.5 },
  "expected_salary_lpa": 22.5,
  "notice_period_days": 30,
  "location": "Bengaluru",
  "open_to_remote": true
}
```

---

## 🗺️ Roadmap

<div align="center">

<table>
<tr>
<td>🔲</td>
<td><b>Resume PDF parsing</b></td>
<td>Extract skills directly from uploaded resumes using PyMuPDF + LLM</td>
</tr>
<tr>
<td>🔲</td>
<td><b>LinkedIn profile integration</b></td>
<td>Live candidate data via LinkedIn API for real-world deployment</td>
</tr>
<tr>
<td>🔲</td>
<td><b>Feedback loop</b></td>
<td>Recruiter marks hired/rejected → system learns from outcomes over time</td>
</tr>
<tr>
<td>🔲</td>
<td><b>Multi-JD batch ranking</b></td>
<td>Rank candidates across multiple open roles simultaneously</td>
</tr>
<tr>
<td>🔲</td>
<td><b>Bias detection layer</b></td>
<td>Flag potential discrimination signals in JD language and scoring patterns</td>
</tr>
<tr>
<td>🔲</td>
<td><b>PostgreSQL + pgvector migration</b></td>
<td>Production-grade horizontal scaling from ChromaDB</td>
</tr>
</table>

</div>

---

## 🔑 Getting a Free Groq API Key

```
1. Visit   →  https://console.groq.com
2. Sign up    (free — no credit card required)
3. Go to   →  API Keys → Create API Key
4. Add to  →  .env as GROQ_API_KEY=your_key_here
```

> **No key?** RecruitMind AI automatically falls back to rule-based offline mode. All semantic search, scoring, and ranking still works fully — only LLM-based JD parsing and explanation generation switches to deterministic rules.

---

## 📁 Key Files Reference

<div align="center">

| File | Role |
|:----:|:----:|
| `pipeline/ranker.py` | 🧠 LangGraph graph — the core brain of the system |
| `pipeline/scorer.py` | 📊 All 5 scoring functions + composite calculator |
| `pipeline/jd_parser.py` | 🤖 Groq LLM + offline JD structured extraction |
| `pipeline/embedder.py` | 🔢 ChromaDB indexing + semantic search engine |
| `pipeline/explainer.py` | 💬 LLM + rule-based recruiter note generator |
| `api/main.py` | ⚡ FastAPI with 6 REST endpoints |
| `ui/app.py` | 🎨 Full Streamlit recruiter dashboard |
| `data/generate_candidates.py` | 👥 100-candidate synthetic dataset generator |
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

## ⚖️ New Features

### Candidate Comparison (`POST /compare`)
Compare 2–3 candidates side by side with full score breakdown.
```json
{
  "candidate_ids": ["CAND_0042", "CAND_0017", "CAND_0063"],
  "jd_text": "Senior Python ML Engineer..."
}
```

### JD Bias Checker (`POST /bias-check`)
Checks any job description for potentially biased language before posting.
```json
{ "jd_text": "We are looking for a young energetic developer..." }
```
Returns bias level (Low/Medium/High), flagged terms, and suggestions for inclusive rewriting.

### Expanded Dataset
System now indexes **300 synthetic candidate profiles** for more realistic and diverse ranking results.

---

## 🤝 Contributing

```bash
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
*T. John Institute of Technology, Bengaluru · CGPA: 8.7 · Expected Graduation: 2027*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-vinaybabannavar--create-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vinaybabannavar-create)

<br/>

![Azure AI-900](https://img.shields.io/badge/Microsoft-AI--900-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![Azure AZ-900](https://img.shields.io/badge/Microsoft-AZ--900-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-Certified-1BA0D7?style=flat-square&logo=cisco&logoColor=white)
![NPTEL](https://img.shields.io/badge/NPTEL-Python-FF6B35?style=flat-square)

<br/>

*Redrob AI × Hack2Skill — INDIA.RUNS Hackathon 2026 · Data & AI Challenge: Intelligent Candidate Discovery*

<br/>

</div>

---

## 📄 License

Licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

**Built with ❤️ using LangGraph · ChromaDB · Groq · FastAPI · Streamlit**

*RecruitMind AI — Because great candidates deserve to be found.*

<br/>

⭐ **If this project impressed you, please star it!** ⭐

</div>
