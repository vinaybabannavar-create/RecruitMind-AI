<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=250&section=header&text=RecruitMind%20AI&fontSize=90&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Next-Generation%20Agentic%20Talent%20Discovery%20Platform&descAlignY=62&descSize=22" width="100%"/>

<br/>

[![Stars](https://img.shields.io/github/stars/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=starship&color=f5a623&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/stargazers)
[![Forks](https://img.shields.io/github/forks/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=git&color=7c3aed&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/network/members)
[![CI](https://img.shields.io/github/actions/workflow/status/vinaybabannavar-create/RecruitMind-AI/ci.yml?style=for-the-badge&label=CI%20Tests&logo=githubactions&logoColor=white&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/actions)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&labelColor=1a1a2e)](LICENSE)
[![Hackathon](https://img.shields.io/badge/Redrob_AI-Hackathon_2026-FF4B4B?style=for-the-badge&logo=rocket&logoColor=white&labelColor=1a1a2e)](https://hack2skill.com)
[![Submitted](https://img.shields.io/badge/Status-Submitted_✓-22C55E?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=1a1a2e)](https://github.com/vinaybabannavar-create/RecruitMind-AI)

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-6_Node_Pipeline-6C63FF?style=for-the-badge)](https://langchain-ai.github.io/langgraph)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Search-F97316?style=for-the-badge)](https://www.trychroma.com)
[![Groq](https://img.shields.io/badge/Groq-Llama--3.3--70B-22C55E?style=for-the-badge)](https://groq.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Candidates](https://img.shields.io/badge/Dataset-300_Profiles-8B5CF6?style=for-the-badge&logo=database&logoColor=white)](https://github.com/vinaybabannavar-create/RecruitMind-AI)

<br/><br/>

<h2>🧠 Where AI meets hiring intelligence</h2>
<h3>Paste a Job Description → AI ranks 300 candidates → Explained shortlist in seconds</h3>

<br/>

**[🚀 Overview](#-overview) · [🏗️ Architecture](#-system-architecture) · [🧠 Pipeline](#-langgraph-agentic-pipeline) · [🔬 Scoring](#-multi-signal-scoring-engine) · [✨ Features](#-new-features) · [⚙️ Setup](#-setup--installation) · [📡 API](#-api-reference) · [🎨 UI](#-ui-features) · [🐳 Docker](#-docker-deployment)**

</div>

---

## 🚀 Overview

**RecruitMind AI** is a fully agentic, production-ready AI recruitment intelligence platform built on a **6-node LangGraph stateful pipeline**. It evaluates **300 candidate profiles** against any job description using semantic vector search, LLM-powered cognitive JD parsing, multi-signal composite scoring, explainable AI reasoning, JD bias detection, and side-by-side candidate comparison.

<div align="center">

<br/>

> ### 💡 Traditional ATS filters by keywords. RecruitMind AI understands intent.

<br/>

<table>
<thead>
<tr>
<th align="center">❌ Traditional ATS</th>
<th align="center">✅ RecruitMind AI</th>
</tr>
</thead>
<tbody>
<tr>
<td>Keyword matching only</td>
<td>🧠 LLM semantic intent understanding — extracts implicit requirements</td>
</tr>
<tr>
<td>Binary pass / fail filter</td>
<td>📊 5-signal weighted composite scoring across multiple dimensions</td>
</tr>
<tr>
<td>No explanation given</td>
<td>💬 Per-candidate AI recruiter notes grounded in actual data</td>
</tr>
<tr>
<td>Homogeneous shortlist</td>
<td>🔁 Diversity-aware re-ranking across seniority and role types</td>
</tr>
<tr>
<td>Complete black box</td>
<td>🔍 Full transparent score breakdown — 5 signals per candidate</td>
</tr>
<tr>
<td>No bias awareness</td>
<td>⚖️ POST /bias-check — flags discriminatory JD language automatically</td>
</tr>
<tr>
<td>No comparison tool</td>
<td>📊 POST /compare — side-by-side analysis of 2-3 candidates</td>
</tr>
<tr>
<td>Fails without internet</td>
<td>🌐 Rule-based offline fallback — always works without API key</td>
</tr>
</tbody>
</table>

</div>

<br/>

### ✨ What Makes RecruitMind AI Extraordinary

<table>
<tr>
<td width="50%" valign="top">

**🔍 Cognitive JD Parsing**
LLM extracts skills, seniority, culture signals, and *implicit* requirements — not just keywords. Understands nuanced JDs the way a senior recruiter would.

**📊 Multi-Signal Scoring Engine**
Composite scores from 5 independent signals — semantic fit, skill match, career growth, GitHub activity, experience fit. Weighted and combined mathematically.

**💡 Explainable AI Shortlists**
Every candidate gets a 3-4 sentence recruiter note generated by Groq Llama-3.3-70B — grounded strictly in real profile data. Zero hallucination.

**🎯 Semantic Vector Search**
ChromaDB + Sentence Transformers (all-MiniLM-L6-v2) for deep contextual matching. Finds a "data pipeline architect" for a "data engineer" JD even without exact keyword match.

</td>
<td width="50%" valign="top">

**⚡ LangGraph Agentic Pipeline**
Modular, observable, stateful 6-node pipeline with fully typed `RankingState`. Each node independently testable. Easy to extend without touching other nodes.

**🔁 Diversity Re-ranking**
Prevents shortlist homogeneity — applies 0.95x penalty to over-represented seniority/role types ensuring balanced, varied candidate selection.

**⚖️ JD Bias Detection**
POST `/bias-check` scans any JD for discriminatory language — age, gender, origin, marital status bias. Returns flagged terms with inclusive rewrite suggestions.

**📊 Candidate Comparison**
POST `/compare` — select 2-3 candidates for full side-by-side score breakdown directly in the Streamlit UI. Unique feature no other team has built.

</td>
</tr>
</table>

---

## 🏗️ System Architecture

<div align="center">
  <img src="assets/RecruitMind-AI.jpg" alt="RecruitMind AI System Architecture" width="100%">
</div>

### 📁 Project Structure

```
RecruitMind-AI/
│
├── 📂 api/
│   ├── main.py              # FastAPI — 8 endpoints: /rank /explain /index /candidates
│   │                        #           /health /candidate/{id} /compare /bias-check
│   └── __init__.py
│
├── 📂 pipeline/
│   ├── jd_parser.py         # Groq LLM + offline heuristic JD structured extraction
│   ├── embedder.py          # Sentence Transformers + ChromaDB indexing & search
│   ├── scorer.py            # 5-signal composite scoring functions
│   ├── ranker.py            # LangGraph 6-node typed state graph — brain of system
│   ├── explainer.py         # Groq LLM + rule-based recruiter note generator
│   └── __init__.py
│
├── 📂 data/
│   ├── generate_candidates.py   # 300 synthetic realistic profile generator
│   └── candidates.json          # Pre-generated dataset — 300 candidates ready
│
├── 📂 ui/
│   └── app.py               # Streamlit dashboard — dark theme, comparison UI, bias checker
│
├── 📂 .github/workflows/
│   └── ci.yml               # GitHub Actions — automated tests on every push
│
├── .env.example             # Environment variables template
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.sh                   # One-command startup script
├── LICENSE
└── README.md
```

---

## 🧠 LangGraph Agentic Pipeline

<div align="center">

The entire ranking process runs as a **LangGraph stateful graph** — each stage is an independent, testable node operating on a shared typed `RankingState`. No node can be skipped or fail silently.

<br/>

<table width="82%" align="center">
<tr>
<td align="center" style="background:#0F172A;color:#A5B4FC;padding:10px;border-radius:8px;border:1px solid #312E81">
<b>📄 JD INPUT</b> &nbsp;—&nbsp; Raw job description text, any length, any format
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td style="background:#1E1B4B;color:white;padding:16px;border-radius:8px;border-left:5px solid #6C63FF">
<b>🟣 Node 1 — <code>parse_jd</code></b><br/>
<b>Groq Llama-3.3-70B</b> (or offline fallback)<br/>
Extracts → Job title · Required skills · Nice-to-have skills · Seniority level · Culture signals · Implicit expectations<br/>
<sub>⟶ Output: Structured JSON dict with all fields</sub>
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td style="background:#1E3A5F;color:white;padding:16px;border-radius:8px;border-left:5px solid #0EA5E9">
<b>🔵 Node 2 — <code>embed_jd</code></b><br/>
<b>sentence-transformers</b> (all-MiniLM-L6-v2)<br/>
Converts structured JD text → 384-dimensional dense vector · CPU-only · ~80MB model · No GPU required<br/>
<sub>⟶ Output: Float vector [384-dim] for cosine similarity search</sub>
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td style="background:#1A3A2A;color:white;padding:16px;border-radius:8px;border-left:5px solid #22C55E">
<b>🟢 Node 3 — <code>retrieve</code></b><br/>
<b>ChromaDB</b> cosine similarity search over 300 indexed candidate vectors<br/>
Returns top-20 most semantically similar profiles with similarity scores attached<br/>
<sub>⟶ Output: List of candidates with semantic_score per profile</sub>
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td style="background:#3A1A00;color:white;padding:16px;border-radius:8px;border-left:5px solid #F97316">
<b>🟠 Node 4 — <code>score</code></b><br/>
<b>Multi-Signal Composite Scoring</b><br/>
Signal 1: Semantic similarity (35%) · Signal 2: Skill match (30%) · Signal 3: Career growth (15%)<br/>
Signal 4: Activity signal (10%) · Signal 5: Experience fit (10%)<br/>
<sub>⟶ Output: Composite score 0.0–1.0 per candidate with full breakdown</sub>
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td style="background:#2D1B4E;color:white;padding:16px;border-radius:8px;border-left:5px solid #A855F7">
<b>🟡 Node 5 — <code>rerank</code></b><br/>
<b>Diversity-Aware Re-ranking</b><br/>
Applies 0.95x penalty when seniority level appears 3+ times or role type appears 4+ times<br/>
Ensures balanced shortlist — not 10 identical senior ML engineers when mid-level candidates fit equally<br/>
<sub>⟶ Output: Reranked sorted list with rank numbers assigned</sub>
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td style="background:#064E3B;color:white;padding:16px;border-radius:8px;border-left:5px solid #10B981">
<b>💬 Node 6 — <code>explain</code></b><br/>
<b>Groq Llama-3.3-70B</b> (or deterministic rule-based fallback)<br/>
Generates 3-4 sentence recruiter-style note per candidate — grounded strictly in actual data and scores<br/>
Zero hallucination: model is seeded with real sub-scores and instructed to only reference existing data<br/>
<sub>⟶ Output: Final ranked shortlist with natural language explanation per candidate</sub>
</td>
</tr>
<tr><td align="center" style="padding:4px;color:#64748B">⬇</td></tr>
<tr>
<td align="center" style="background:#0F172A;color:white;padding:14px;border-radius:8px;border:2px solid #6C63FF">
<b>✅ RANKED SHORTLIST OUTPUT</b><br/>
<code>rank</code> · <code>composite_score</code> · <code>score_breakdown</code> (5 signals) · <code>explanation</code> · <code>metadata</code> · <code>processing_time_sec</code>
</td>
</tr>
</table>

</div>

> **State is fully typed** using Python `TypedDict` — every node receives and emits the complete `RankingState`, making each stage independently testable, inspectable, and extensible without touching other nodes.

---

## 🔬 Multi-Signal Scoring Engine

<div align="center">

Every candidate receives a **composite score built from 5 independent signals** — each measuring a completely different dimension of fit. No single signal dominates.

<br/>

<table>
<thead>
<tr>
<th align="center">Signal</th>
<th align="center">Weight</th>
<th>Algorithm</th>
<th align="center">Range</th>
</tr>
</thead>
<tbody>
<tr>
<td>🧬 <b>Semantic Similarity</b></td>
<td align="center"><b>35%</b></td>
<td>Cosine distance — JD vector vs candidate profile vector via ChromaDB</td>
<td align="center">0.0 – 1.0</td>
</tr>
<tr>
<td>🛠️ <b>Skill Match</b></td>
<td align="center"><b>30%</b></td>
<td>Required skills hit rate × 0.8 + nice-to-have bonus × 0.2</td>
<td align="center">0.0 – 1.0</td>
</tr>
<tr>
<td>📈 <b>Career Growth</b></td>
<td align="center"><b>15%</b></td>
<td>Raw growth score × 0.6 + tenure stability × 0.3 + promotions bonus</td>
<td align="center">0.0 – 1.0</td>
</tr>
<tr>
<td>⚡ <b>Activity Signal</b></td>
<td align="center"><b>10%</b></td>
<td>GitHub score × 0.5 + LeetCode × 0.3 + hackathons × 0.2 × recency multiplier</td>
<td align="center">0.0 – 1.0</td>
</tr>
<tr>
<td>📅 <b>Experience Fit</b></td>
<td align="center"><b>10%</b></td>
<td>Linear penalty for under/over-experience × seniority level alignment multiplier</td>
<td align="center">0.0 – 1.0</td>
</tr>
</tbody>
</table>

<br/>

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║   Composite = (0.35 × Semantic) + (0.30 × Skill) + (0.15 × Career)             ║
║                     + (0.10 × Activity) + (0.10 × ExperienceFit)                ║
║                                                                                  ║
║   ↓  Diversity Re-ranker (0.95× penalty for over-represented types)             ║
║   ↓  Sort descending → Top-K shortlist → AI explanation per candidate           ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## ✨ New Features

<div align="center">

<table>
<tr>
<td width="33%" align="center" style="padding:16px">

### ⚖️ JD Bias Checker
**`POST /bias-check`**

Scans any job description for potentially discriminatory language before posting.

Detects: age bias · gender bias · origin bias · marital status bias

Returns: Bias level (Low/Medium/High) · Flagged terms · Inclusive rewrite suggestions

</td>
<td width="33%" align="center" style="padding:16px">

### 📊 Candidate Comparison
**`POST /compare`**

Select 2–3 candidates from the shortlist for a full side-by-side score breakdown.

Shows: All 5 signal scores · Skills · Certifications · Experience — in parallel columns

Available directly in the Streamlit dashboard UI

</td>
<td width="33%" align="center" style="padding:16px">

### 👥 300 Candidate Dataset
**Expanded from 100 → 300**

More diverse, realistic profiles across ML, Backend, Fullstack, DevOps, Data Engineering roles

More variety in location, seniority, skills, GitHub activity, and salary expectations

</td>
</tr>
</table>

</div>

---

## ⚙️ Setup & Installation

### Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Python | 3.11+ | Required |
| pip | Latest | Required |
| Git | Any | Required |
| Groq API Key | — | **Optional** — system works fully without it |

---

### ⚡ Option A — One-Command Startup (Recommended)

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
bash run.sh
```

> `run.sh` handles everything: install dependencies → setup env → generate 300 candidates → index into ChromaDB → start API → launch Streamlit UI.

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

**Step 5 — Generate + Index 300 candidates**
```bash
python data/generate_candidates.py
# Output: data/candidates.json (300 synthetic profiles)

python -c "from pipeline.embedder import get_engine; get_engine().index_candidates()"
# Embeds all 300 candidates and stores in data/chroma_db/
```

**Step 6 — Start (two terminals)**
```bash
# Terminal 1 — FastAPI
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2 — Streamlit
streamlit run ui/app.py --server.port 8501
```

Open **http://localhost:8501** 🎉

---

## 📡 API Reference

<div align="center">

| Method | Endpoint | Description |
|:------:|:--------:|:------------|
| `POST` | `/rank` | 🎯 Full pipeline — JD in, ranked shortlist out with AI explanations |
| `GET` | `/health` | 💚 System health, indexing status, LLM availability |
| `GET` | `/candidates` | 📋 Paginated list of all 300 candidates |
| `GET` | `/candidate/{id}` | 👤 Single candidate profile by ID |
| `POST` | `/index` | 🔄 Re-index candidates into ChromaDB (background) |
| `POST` | `/explain` | 💬 Add AI explanations to an existing shortlist |
| `POST` | `/compare` | ⚖️ Side-by-side comparison of 2-3 candidates |
| `POST` | `/bias-check` | 🔍 Check JD for potentially biased language |

</div>

> 📖 Full interactive Swagger docs at **http://localhost:8000/docs**

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

### `POST /compare` — Candidate Comparison

```json
{
  "candidate_ids": ["CAND_0042", "CAND_0017", "CAND_0063"],
  "jd_text": "Senior Python ML Engineer..."
}
```

### `POST /bias-check` — JD Bias Detection

```json
{ "jd_text": "We are looking for a young energetic developer..." }
```

**Response:**
```json
{
  "bias_flags": [
    {
      "term": "young",
      "reason": "May indicate age bias",
      "suggestion": "Use skills-based language instead"
    }
  ],
  "bias_level": "Medium",
  "bias_score": 20,
  "total_flags": 1,
  "recommendation": "Review and rewrite flagged sections using inclusive, skills-focused language."
}
```

### `GET /health`

```json
{
  "status": "ok",
  "candidates_indexed": 300,
  "vector_db_ready": true,
  "llm_available": true,
  "version": "1.0.0"
}
```

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
<td>Paste any job description + 5 one-click quick-fill templates (ML / Backend / Fullstack / Data / DevOps)</td>
</tr>
<tr>
<td>🔄 <b>Live Pipeline Stepper</b></td>
<td>Real-time animated progress: Parsing JD → Embedding → Searching 300 candidates → Scoring → Explaining</td>
</tr>
<tr>
<td>🔗 <b>Live API Status Sidebar</b></td>
<td>Shows: system online status · 300 candidates indexed · LLM mode · version</td>
</tr>
<tr>
<td>🎛️ <b>Interactive Filters</b></td>
<td>Filter by location · Min match % · Max notice days · Max salary (LPA) — all real-time</td>
</tr>
<tr>
<td>📊 <b>Summary Metrics Bar</b></td>
<td>Filtered shortlist count · Total evaluated · Processing time · Skills extracted · Seniority level</td>
</tr>
<tr>
<td>🔍 <b>Parsed JD Expander</b></td>
<td>See exactly what AI extracted from your JD — skills, seniority, culture signals, implicit expectations</td>
</tr>
<tr>
<td>🏆 <b>Ranked Leaderboard</b></td>
<td>Sortable table: rank · name · match % · experience · skills hit · location · salary · notice</td>
</tr>
<tr>
<td>📋 <b>Detailed Profile Cards</b></td>
<td>Expandable per-candidate view with complete profile, GitHub stats, LeetCode, certifications</td>
</tr>
<tr>
<td>💬 <b>AI Recruiter Notes</b></td>
<td>LLM-generated explanation card per candidate — grounded in data, not hallucinated</td>
</tr>
<tr>
<td>🟢 <b>Skill Match Highlighting</b></td>
<td>Green tags = matched required skills · Grey tags = additional skills candidate has</td>
</tr>
<tr>
<td>📈 <b>Score Breakdown Bars</b></td>
<td>Color-coded visual bars for all 5 signals: green ≥80% · orange 65-79% · red &lt;65%</td>
</tr>
<tr>
<td>⚖️ <b>Side-by-Side Comparison</b></td>
<td>Select 2-3 candidates → compare all 5 signal scores in parallel columns</td>
</tr>
<tr>
<td>🔎 <b>JD Bias Checker</b></td>
<td>Paste any JD → instant bias level + flagged terms + rewrite suggestions</td>
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
pytest tests/ -v                    # all tests
pytest tests/test_scorer.py -v     # scoring tests only
```

---

## 🐳 Docker Deployment

> No local Python setup needed. One command runs the full stack.

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
cp .env.example .env             # add GROQ_API_KEY (optional)
docker-compose up --build
```

<div align="center">

| Service | URL | Description |
|:-------:|:---:|:-----------|
| 🎨 Streamlit UI | http://localhost:8501 | Full recruiter dashboard |
| ⚡ FastAPI Backend | http://localhost:8000 | 8 REST endpoints |
| 📖 API Docs | http://localhost:8000/docs | Interactive Swagger UI |

</div>

```bash
docker-compose down    # stop all services
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
<td>Free API · Fastest open-weight LLM · Excellent instruction following for JD parsing</td>
</tr>
<tr>
<td>🔢 <b>Embeddings</b></td>
<td>sentence-transformers (all-MiniLM-L6-v2)</td>
<td>3.0.1</td>
<td>CPU-only · 80MB · High-quality 384-dim vectors · No API cost</td>
</tr>
<tr>
<td>🗃️ <b>Vector DB</b></td>
<td>ChromaDB (persistent)</td>
<td>0.5.3</td>
<td>In-process · No external server · Cosine similarity built-in · Simple Python API</td>
</tr>
<tr>
<td>⚡ <b>Orchestration</b></td>
<td>LangGraph</td>
<td>0.2.14</td>
<td>Stateful typed pipeline · Each node independently testable · Natural fit for agentic ranking</td>
</tr>
<tr>
<td>🌐 <b>Backend API</b></td>
<td>FastAPI + Uvicorn</td>
<td>0.115</td>
<td>Async Python REST · Auto Swagger docs · Pydantic validation · Production performance</td>
</tr>
<tr>
<td>🎨 <b>Frontend</b></td>
<td>Streamlit</td>
<td>1.39</td>
<td>Rapid recruiter dashboard · Live updates · Minimal frontend code</td>
</tr>
<tr>
<td>🐳 <b>Deployment</b></td>
<td>Docker + Compose</td>
<td>Latest</td>
<td>Single-command reproducible full-stack deployment with persistent volume</td>
</tr>
<tr>
<td>🔄 <b>CI/CD</b></td>
<td>GitHub Actions</td>
<td>—</td>
<td>Automated tests on every push — verifies imports, logic, dataset integrity</td>
</tr>
<tr>
<td>📦 <b>Data</b></td>
<td>Python synthetic generator</td>
<td>—</td>
<td>300 realistic profiles · 20+ fields · skills, GitHub, career, activity signals</td>
</tr>
</tbody>
</table>

</div>

---

## 🗂️ Candidate Data Schema

Each of the **300 synthetic candidates** carries a rich, realistic profile with 20+ fields:

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
  "github": {
    "repos": 24,
    "contributions_last_year": 380,
    "open_source_prs": 14,
    "github_score": 0.82
  },
  "activity_signals": {
    "leetcode_solved": 210,
    "hackathon_participations": 4,
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

## 📁 Key Files Reference

<div align="center">

| File | Role |
|:----:|:-----|
| `pipeline/ranker.py` | 🧠 LangGraph 6-node graph — the core brain of the entire system |
| `pipeline/scorer.py` | 📊 All 5 scoring functions + weighted composite calculator |
| `pipeline/jd_parser.py` | 🤖 Groq LLM + offline heuristic JD structured extraction |
| `pipeline/embedder.py` | 🔢 ChromaDB indexing + semantic search over 300 profiles |
| `pipeline/explainer.py` | 💬 Groq LLM + rule-based recruiter note generator |
| `api/main.py` | ⚡ FastAPI with 8 REST endpoints |
| `ui/app.py` | 🎨 Streamlit dashboard — dark theme, comparison UI, bias checker |
| `data/generate_candidates.py` | 👥 300-candidate synthetic realistic dataset generator |
| `run.sh` | 🚀 One-command startup — install → generate → index → API → UI |
| `docker-compose.yml` | 🐳 Full stack orchestration with persistent ChromaDB volume |

</div>

---

## 🗺️ Roadmap

<div align="center">

<table>
<tr>
<td align="center">🔲</td>
<td><b>Resume PDF parsing</b></td>
<td>Extract skills directly from uploaded candidate resumes using PyMuPDF + LLM</td>
</tr>
<tr>
<td align="center">🔲</td>
<td><b>LinkedIn profile integration</b></td>
<td>Live candidate data via LinkedIn API for real-world production deployment</td>
</tr>
<tr>
<td align="center">🔲</td>
<td><b>Feedback loop learning</b></td>
<td>Recruiter marks hired/rejected → system learns and improves scoring weights</td>
</tr>
<tr>
<td align="center">🔲</td>
<td><b>Multi-JD batch ranking</b></td>
<td>Rank all candidates across multiple open roles simultaneously</td>
</tr>
<tr>
<td align="center">🔲</td>
<td><b>PostgreSQL + pgvector</b></td>
<td>Production-grade horizontal scaling migration from ChromaDB</td>
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

> **No key?** RecruitMind AI auto-falls back to rule-based offline mode. All semantic search, ChromaDB retrieval, composite scoring, and ranking still works fully. Only LLM-based JD parsing and explanation generation switches to deterministic rules.

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

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=130&section=footer" width="100%"/>

**Built with ❤️ using LangGraph · ChromaDB · Groq · FastAPI · Streamlit**

*RecruitMind AI — Because great candidates deserve to be found.*

<br/>

⭐ **If this project impressed you, please star it!** ⭐

</div>
