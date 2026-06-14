cat > /mnt/user-data/outputs/README.md << 'READMEEOF'
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=250&section=header&text=RecruitMind%20AI&fontSize=95&fontColor=fff&animation=twinkling&fontAlignY=40&desc=🧠%20Next-Generation%20Agentic%20Talent%20Discovery%20Platform&descAlignY=65&descSize=22" width="100%"/>

<br/>

[![Stars](https://img.shields.io/github/stars/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=starship&color=f5a623&labelColor=0f0f1a)](https://github.com/vinaybabannavar-create/RecruitMind-AI/stargazers)
[![Forks](https://img.shields.io/github/forks/vinaybabannavar-create/RecruitMind-AI?style=for-the-badge&logo=git&color=7c3aed&labelColor=0f0f1a)](https://github.com/vinaybabannavar-create/RecruitMind-AI/network/members)
[![CI](https://img.shields.io/github/actions/workflow/status/vinaybabannavar-create/RecruitMind-AI/ci.yml?style=for-the-badge&label=CI%20Pipeline&logo=githubactions&logoColor=white&labelColor=0f0f1a&color=22c55e)](https://github.com/vinaybabannavar-create/RecruitMind-AI/actions)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white&labelColor=0f0f1a)](LICENSE)

<br/>

[![Hackathon](https://img.shields.io/badge/🏆_Redrob_AI-Hackathon_2026-FF4B4B?style=for-the-badge&labelColor=0f0f1a)](https://hack2skill.com)
[![Challenge](https://img.shields.io/badge/🎯_Challenge-Intelligent_Candidate_Discovery-6C63FF?style=for-the-badge&labelColor=0f0f1a)](https://hack2skill.com)
[![Status](https://img.shields.io/badge/✅_Status-Submitted-22C55E?style=for-the-badge&labelColor=0f0f1a)](https://github.com/vinaybabannavar-create/RecruitMind-AI)
[![Dataset](https://img.shields.io/badge/📦_Dataset-300_Candidates-F97316?style=for-the-badge&labelColor=0f0f1a)](https://github.com/vinaybabannavar-create/RecruitMind-AI)

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_Pipeline-6C63FF?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain-ai.github.io/langgraph)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Search-F97316?style=for-the-badge&logo=databricks&logoColor=white)](https://www.trychroma.com)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-22C55E?style=for-the-badge&logo=meta&logoColor=white)](https://groq.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Sentence Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-8B5CF6?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co)

<br/><br/>

<h2>🧠 Where AI meets hiring intelligence.</h2>
<h3>Paste a Job Description → AI thinks like a recruiter → Ranked shortlist in seconds.</h3>

<br/>

<a href="#-overview">🚀 Overview</a> &nbsp;·&nbsp;
<a href="#-system-architecture">🏗️ Architecture</a> &nbsp;·&nbsp;
<a href="#-langgraph-agentic-pipeline">🧠 Pipeline</a> &nbsp;·&nbsp;
<a href="#-multi-signal-scoring-engine">🔬 Scoring</a> &nbsp;·&nbsp;
<a href="#-setup--installation">⚙️ Setup</a> &nbsp;·&nbsp;
<a href="#-api-reference">📡 API</a> &nbsp;·&nbsp;
<a href="#-ui-features">🎨 UI</a> &nbsp;·&nbsp;
<a href="#-docker-deployment">🐳 Docker</a> &nbsp;·&nbsp;
<a href="#-new-features">⚖️ New</a>

</div>

---

## 🚀 Overview

**RecruitMind AI** is a fully agentic, production-ready AI recruitment intelligence platform built on a **6-node LangGraph stateful pipeline**. It moves far beyond keyword filtering — using semantic vector search, LLM-powered cognitive JD parsing, multi-signal composite scoring, and explainable AI reasoning to surface the *exact right candidates* for any job description — ranked, explained, and ready to hire.

<div align="center">

<br/>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    📄 Paste JD  →  🧠 AI Parses Intent  →  🔍 Semantic Search               ║
║    📊 Multi-Signal Score  →  💬 AI Explains  →  ✅ Ranked Shortlist          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

<br/>

<table>
<thead>
<tr>
<th width="50%">❌ Traditional ATS</th>
<th width="50%">✅ RecruitMind AI</th>
</tr>
</thead>
<tbody>
<tr>
<td>Keyword matching only</td>
<td>🧠 LLM semantic intent understanding</td>
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
<td>Homogeneous shortlists</td>
<td>🔁 Diversity-aware re-ranking</td>
</tr>
<tr>
<td>Complete black box</td>
<td>🔍 Full transparent score breakdown</td>
</tr>
<tr>
<td>Crashes without API</td>
<td>🌐 Rule-based offline fallback</td>
</tr>
<tr>
<td>No bias awareness</td>
<td>⚖️ JD bias detection built-in</td>
</tr>
<tr>
<td>No comparison feature</td>
<td>🆚 Side-by-side candidate comparison</td>
</tr>
</tbody>
</table>

</div>

<br/>

### ✨ Key Highlights

<table>
<tr>
<td width="50%" valign="top">

🔍 **Cognitive JD Parsing**
LLM extracts skills, seniority, culture signals, and *implicit* requirements — not just keywords

📊 **Multi-Signal Scoring Engine**
5 independent weighted signals measuring every dimension of candidate fit

💡 **Explainable AI Shortlists**
Every candidate gets a natural language recruiter note from Groq Llama-3.3-70B

🎯 **Semantic Vector Search**
ChromaDB + all-MiniLM-L6-v2 for deep contextual matching beyond surface keywords

</td>
<td width="50%" valign="top">

⚡ **LangGraph Agentic Pipeline**
Modular, observable, stateful 6-node pipeline with fully typed `RankingState`

🔁 **Diversity Re-ranking**
0.95× penalty prevents homogeneous shortlists across seniority and role types

⚖️ **JD Bias Checker**
Flags age, gender, and origin bias in job descriptions before posting

🆚 **Candidate Comparison**
Side-by-side comparison of 2-3 candidates with full score breakdown

</td>
</tr>
</table>

---

## 🏗️ System Architecture

<div align="center">

<br/>

<table width="90%">
<tr>
<td colspan="5" align="center" style="background:#0f172a;color:white;padding:14px;border-radius:10px 10px 0 0">
<b>✦ INPUT LAYER ✦</b>
</td>
</tr>
<tr>
<td align="center" width="30%" style="background:#1e1b4b;color:white;padding:12px;border-radius:8px">
📄 <b>Job Description</b><br/><sub>Text / PDF / URL</sub>
</td>
<td align="center" width="5%">·</td>
<td align="center" width="30%" style="background:#1e1b4b;color:white;padding:12px;border-radius:8px">
👤 <b>300 Candidate Profiles</b><br/><sub>Rich JSON with 20+ fields each</sub>
</td>
<td align="center" width="5%">·</td>
<td align="center" width="30%" style="background:#1e1b4b;color:white;padding:12px;border-radius:8px">
📡 <b>Behavioral Signals</b><br/><sub>GitHub · LeetCode · Hackathons</sub>
</td>
</tr>
<tr><td colspan="5" align="center"><br/>⬇️ ⬇️ ⬇️<br/><br/></td></tr>
<tr>
<td colspan="5" align="center" style="background:#1e3a5f;color:white;padding:14px;border-radius:8px">
<b>✦ PROCESSING LAYER ✦</b><br/><br/>
🤖 <b>LLM JD Parser</b> (Groq / Offline) &nbsp;→&nbsp; 🔢 <b>Embedding Engine</b> (sentence-transformers) &nbsp;→&nbsp; 📊 <b>Signal Extractor</b> (heuristics)
</td>
</tr>
<tr><td colspan="5" align="center"><br/>⬇️<br/><br/></td></tr>
<tr>
<td colspan="5" align="center" style="background:#4f46e5;color:white;padding:16px;border-radius:8px">
<b>⚡ ORCHESTRATION — LangGraph Agentic Pipeline</b><br/><br/>
<code>parse_jd</code> → <code>embed_jd</code> → <code>retrieve</code> → <code>score</code> → <code>rerank</code> → <code>explain</code><br/><br/>
<sub>Fully typed RankingState · Each node independently testable · Stateful graph execution</sub>
</td>
</tr>
<tr><td colspan="5" align="center"><br/>⬇️ ⬇️ ⬇️<br/><br/></td></tr>
<tr>
<td align="center" width="30%" style="background:#065f46;color:white;padding:12px;border-radius:8px">
🗃️ <b>ChromaDB</b><br/><sub>Vector store · Cosine similarity · Persistent</sub>
</td>
<td align="center" width="5%">·</td>
<td align="center" width="30%" style="background:#065f46;color:white;padding:12px;border-radius:8px">
📋 <b>Metadata Store</b><br/><sub>candidates.json · 300 profiles</sub>
</td>
<td align="center" width="5%">·</td>
<td align="center" width="30%" style="background:#065f46;color:white;padding:12px;border-radius:8px">
⚡ <b>Cache Layer</b><br/><sub>Redis (optional) · Fast repeat queries</sub>
</td>
</tr>
<tr><td colspan="5" align="center"><br/>⬇️<br/><br/></td></tr>
<tr>
<td align="center" width="30%" style="background:#7c2d12;color:white;padding:12px;border-radius:8px">
🌐 <b>FastAPI REST API</b><br/><sub>8 endpoints · Swagger docs</sub>
</td>
<td align="center" width="5%">→</td>
<td align="center" width="30%" style="background:#7c2d12;color:white;padding:12px;border-radius:8px">
🎨 <b>Streamlit Dashboard</b><br/><sub>Ranked cards · Score bars · AI notes</sub>
</td>
<td align="center" width="5%">→</td>
<td align="center" width="30%" style="background:#7c2d12;color:white;padding:12px;border-radius:8px">
📥 <b>Export</b><br/><sub>JSON · CSV · Excel download</sub>
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
│   ├── main.py          # FastAPI — 8 endpoints: /rank /explain /index /candidates
│   │                    #           /health /candidate/{id} /compare /bias-check
│   └── __init__.py
│
├── 📂 pipeline/
│   ├── jd_parser.py     # Groq LLM + offline JD structured extraction
│   ├── embedder.py      # Sentence Transformers + ChromaDB indexing & search
│   ├── scorer.py        # 5-signal composite scoring functions
│   ├── ranker.py        # LangGraph 6-node state graph — brain of the system
│   ├── explainer.py     # Groq LLM + rule-based recruiter note generator
│   └── __init__.py
│
├── 📂 data/
│   ├── generate_candidates.py   # 300 synthetic profile generator
│   └── candidates.json          # Pre-generated dataset (300 profiles, ready to use)
│
├── 📂 ui/
│   └── app.py           # Streamlit premium recruiter dashboard
│
├── 📂 .github/workflows/
│   └── ci.yml           # GitHub Actions CI — automated tests on every push
│
├── .env.example         # Environment variables template
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── run.sh               # ⚡ One-command startup script
├── LICENSE
└── README.md
```

---

## 🧠 LangGraph Agentic Pipeline

<div align="center">

The entire ranking process runs as a **LangGraph stateful graph** — each stage is an independent, testable node operating on a shared typed `RankingState`. Zero coupling between nodes.

<br/>

<table width="85%">
<tr>
<td align="center" colspan="2" style="background:#0f0f1a;color:white;padding:12px;border-radius:8px;border:2px solid #6c63ff">
📄 <b>JD INPUT</b> — Raw job description text
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td width="8%" align="center" style="background:#4f46e5;color:white;padding:10px;border-radius:8px;font-size:18px"><b>1</b></td>
<td style="background:#1e1b4b;color:white;padding:12px;border-radius:8px;border-left:4px solid #6c63ff">
<b>parse_jd</b> — Groq Llama-3.3-70B (or offline fallback)<br/>
<sub>Extracts: job title · required skills · nice-to-have skills · seniority level · culture signals · implicit expectations → Structured JSON</sub>
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td width="8%" align="center" style="background:#0369a1;color:white;padding:10px;border-radius:8px;font-size:18px"><b>2</b></td>
<td style="background:#1e3a5f;color:white;padding:12px;border-radius:8px;border-left:4px solid #0ea5e9">
<b>embed_jd</b> — sentence-transformers (all-MiniLM-L6-v2)<br/>
<sub>Converts JD → 384-dimensional dense vector · CPU-only · ~80MB model · No GPU required</sub>
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td width="8%" align="center" style="background:#15803d;color:white;padding:10px;border-radius:8px;font-size:18px"><b>3</b></td>
<td style="background:#1a3a2a;color:white;padding:12px;border-radius:8px;border-left:4px solid #22c55e">
<b>retrieve</b> — ChromaDB cosine similarity search<br/>
<sub>Searches 300 indexed candidate vectors · Returns top-20 semantically closest profiles with similarity scores</sub>
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td width="8%" align="center" style="background:#b45309;color:white;padding:10px;border-radius:8px;font-size:18px"><b>4</b></td>
<td style="background:#3a1a00;color:white;padding:12px;border-radius:8px;border-left:4px solid #f97316">
<b>score</b> — Multi-Signal Composite Scoring<br/>
<sub>Semantic (35%) + Skill Match (30%) + Career Growth (15%) + Activity (10%) + Experience Fit (10%) → Composite 0.0–1.0</sub>
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td width="8%" align="center" style="background:#7c3aed;color:white;padding:10px;border-radius:8px;font-size:18px"><b>5</b></td>
<td style="background:#3a1a3a;color:white;padding:12px;border-radius:8px;border-left:4px solid #a855f7">
<b>rerank</b> — Diversity-Aware Re-ranking<br/>
<sub>Applies 0.95× penalty to over-represented seniority/role types · Ensures balanced, diverse shortlist</sub>
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td width="8%" align="center" style="background:#0f766e;color:white;padding:10px;border-radius:8px;font-size:18px"><b>6</b></td>
<td style="background:#1a3a2a;color:white;padding:12px;border-radius:8px;border-left:4px solid #10b981">
<b>explain</b> — Groq Llama-3.3-70B (or rule-based fallback)<br/>
<sub>Generates 3-4 sentence recruiter note per candidate · Grounded in real data · Zero hallucination</sub>
</td>
</tr>
<tr><td colspan="2" align="center">⬇️</td></tr>
<tr>
<td align="center" colspan="2" style="background:#0f0f1a;color:white;padding:12px;border-radius:8px;border:2px solid #22c55e">
✅ <b>RANKED SHORTLIST OUTPUT</b><br/>
<code>rank</code> · <code>composite_score</code> · <code>score_breakdown (5 signals)</code> · <code>explanation</code> · <code>metadata</code> · <code>processing_time_sec</code>
</td>
</tr>
</table>

</div>

> **State is fully typed** using Python `TypedDict` — every node receives and emits the complete `RankingState`, making each stage independently testable, inspectable, and extensible without touching other nodes.

---

## 🔬 Multi-Signal Scoring Engine

<div align="center">

Every candidate receives a **composite score from 5 independent signals** — each measuring a completely different dimension of fit.

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
<td align="center"><b>35%</b></td>
<td>Cosine distance between JD embedding and candidate profile embedding via ChromaDB</td>
<td align="center">0.0–1.0</td>
</tr>
<tr>
<td>🛠️ <b>Skill Match</b></td>
<td align="center"><b>30%</b></td>
<td>Required skills hit rate × 0.8 + nice-to-have bonus × 0.2</td>
<td align="center">0.0–1.0</td>
</tr>
<tr>
<td>📈 <b>Career Growth</b></td>
<td align="center"><b>15%</b></td>
<td>Raw growth score × 0.6 + tenure stability × 0.3 + promotions bonus</td>
<td align="center">0.0–1.0</td>
</tr>
<tr>
<td>⚡ <b>Activity Signal</b></td>
<td align="center"><b>10%</b></td>
<td>GitHub score × 0.5 + LeetCode × 0.3 + hackathons × 0.2 × recency multiplier</td>
<td align="center">0.0–1.0</td>
</tr>
<tr>
<td>📅 <b>Experience Fit</b></td>
<td align="center"><b>10%</b></td>
<td>Linear penalty for under/over-experience × seniority alignment multiplier</td>
<td align="center">0.0–1.0</td>
</tr>
</tbody>
</table>

<br/>

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   Composite = (0.35 × Semantic) + (0.30 × Skill) + (0.15 × Career)         ║
║                    + (0.10 × Activity) + (0.10 × ExperienceFit)             ║
║                                                                              ║
║   → Diversity Re-ranker (0.95× penalty for over-represented types)          ║
║   → Sort descending → Top-K shortlist with AI explanation per candidate     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

## ⚙️ Setup & Installation

### Prerequisites

| Requirement | Version | Notes |
|:-----------:|:-------:|:-----:|
| Python | 3.11+ | Required |
| pip | Latest | Required |
| Git | Any | Required |
| Groq API Key | — | **Optional** — system works without it |

---

### ⚡ Option A — One-Command Startup *(Recommended)*

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
bash run.sh
```

> `run.sh` handles **everything** automatically — dependency install → env setup → candidate generation → ChromaDB indexing → API start → Streamlit launch. Zero manual steps.

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
# Output: data/candidates.json (300 synthetic profiles)

python -c "from pipeline.embedder import get_engine; get_engine().index_candidates()"
# Embeds all 300 candidates into ChromaDB
```

**Step 6 — Start (two terminals)**
```bash
# Terminal 1 — FastAPI Backend
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2 — Streamlit Dashboard
streamlit run ui/app.py --server.port 8501
```

Open **http://localhost:8501** 🎉

---

## 📡 API Reference

<div align="center">

| Method | Endpoint | Description |
|:------:|:--------:|:------------|
| `POST` | `/rank` | 🎯 Full pipeline — JD in, ranked shortlist + AI explanations out |
| `GET` | `/health` | 💚 System health + indexing status |
| `GET` | `/candidates` | 👥 Paginated list of all 300 candidates |
| `GET` | `/candidate/{id}` | 🔎 Single candidate profile by ID |
| `POST` | `/index` | 🔄 Re-index all candidates into ChromaDB |
| `POST` | `/explain` | 💬 Add AI explanations to an existing shortlist |
| `POST` | `/compare` | 🆚 Compare 2-3 candidates side by side |
| `POST` | `/bias-check` | ⚖️ Detect biased language in any JD |

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
      "explanation": "Ranked #1 — strong match on Python, FastAPI and LangChain (85% skill overlap). 5 years senior experience aligns perfectly. Active open source contributor (14 PRs). AWS certified. Ideal fit.",
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
  "bias_flags": [{"term": "young", "reason": "May indicate age bias", "suggestion": "Use skills-based language instead"}],
  "bias_level": "Medium",
  "bias_score": 20,
  "total_flags": 1,
  "recommendation": "Review and rewrite flagged sections using inclusive language."
}
```

> 📖 Full interactive Swagger docs at **http://localhost:8000/docs**

---

## 🎨 UI Features

<div align="center">

*The Streamlit dashboard is built for a recruiter who needs answers fast — dark-themed, intelligent, and visually rich.*

<br/>

<table>
<thead>
<tr>
<th>🖥️ Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>📋 <b>JD Input Panel</b></td>
<td>Paste any JD + 5 one-click industry quick-fill templates (ML, Backend, Full Stack, Data, DevOps)</td>
</tr>
<tr>
<td>🔄 <b>Live Pipeline Stepper</b></td>
<td>Real-time animated progress — JD Processed → Vector Search → Multi-Signal Score → Llama Recruiter Note</td>
</tr>
<tr>
<td>🟢 <b>System Status Panel</b></td>
<td>Live sidebar: System Online · 300 candidates indexed · LLM: Groq Llama-3.3 · v1.0.0</td>
</tr>
<tr>
<td>📊 <b>Summary Metrics Bar</b></td>
<td>Filtered shortlist · Total evaluated · Processing time · Skills extracted · Seniority level</td>
</tr>
<tr>
<td>🔍 <b>Parsed JD Expander</b></td>
<td>Expandable view of AI-extracted structure — skills, seniority, implicit expectations</td>
</tr>
<tr>
<td>🏆 <b>Ranked Leaderboard</b></td>
<td>Sortable table: Rank · Name · Match % · Experience · Skills Hit · Location · Salary · Notice</td>
</tr>
<tr>
<td>📋 <b>Detailed Profile Cards</b></td>
<td>Per-candidate expandable card with score ring, AI recruiter note, skill tags, score breakdown bars</td>
</tr>
<tr>
<td>🟢 <b>Skill Highlighting</b></td>
<td>Green tags = matched JD requirements · Grey tags = additional candidate skills</td>
</tr>
<tr>
<td>📈 <b>Score Breakdown Bars</b></td>
<td>Color-coded visual bars for all 5 signals — green ≥80% · amber 65-79% · red &lt;65%</td>
</tr>
<tr>
<td>🆚 <b>Side-by-Side Comparison</b></td>
<td>Select 2-3 candidates → compare scores, skills, experience in parallel columns</td>
</tr>
<tr>
<td>⚖️ <b>JD Bias Checker</b></td>
<td>Paste any JD → instant bias scan → flagged terms + inclusive rewrite suggestions</td>
</tr>
<tr>
<td>🔽 <b>Interactive Filters</b></td>
<td>Filter by location, min match %, max salary, max notice period — live re-filtering</td>
</tr>
<tr>
<td>📥 <b>Export Results</b></td>
<td>Download full results as <b>JSON</b> or ranked shortlist as <b>CSV</b></td>
</tr>
</tbody>
</table>

</div>

---

## ⚖️ New Features

<div align="center">

<table>
<tr>
<td align="center" width="33%" style="background:#1e1b4b;color:white;padding:16px;border-radius:10px">
<h3>🆚 Candidate Comparison</h3>
<b>POST /compare</b><br/><br/>
Compare 2–3 candidates side by side with full score breakdown per signal. Available in both API and Streamlit UI.
</td>
<td width="2%"></td>
<td align="center" width="33%" style="background:#14532d;color:white;padding:16px;border-radius:10px">
<h3>⚖️ JD Bias Checker</h3>
<b>POST /bias-check</b><br/><br/>
Scans any JD for age, gender, origin, and marital bias. Returns bias score 0-100, flagged terms, and rewrite suggestions.
</td>
<td width="2%"></td>
<td align="center" width="33%" style="background:#7c2d12;color:white;padding:16px;border-radius:10px">
<h3>📦 300 Candidates</h3>
<b>Expanded Dataset</b><br/><br/>
System now indexes 300 synthetic realistic candidate profiles — 3× more diverse for robust ranking results.
</td>
</tr>
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

> No local Python setup needed. One command brings the entire stack online.

```bash
git clone https://github.com/vinaybabannavar-create/RecruitMind-AI.git
cd RecruitMind-AI
cp .env.example .env             # Add GROQ_API_KEY (optional)
docker-compose up --build
```

<div align="center">

| Service | URL | Description |
|:-------:|:---:|:------------|
| 🎨 Streamlit UI | http://localhost:8501 | Full recruiter dashboard |
| ⚡ FastAPI Backend | http://localhost:8000 | REST API with 8 endpoints |
| 📖 API Docs | http://localhost:8000/docs | Interactive Swagger UI |

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
<td>Free tier, fastest open-weight inference, excellent instruction following for JD parsing</td>
</tr>
<tr>
<td>🔢 <b>Embeddings</b></td>
<td>sentence-transformers (all-MiniLM-L6-v2)</td>
<td>3.0.1</td>
<td>CPU-only, 80MB, high-quality 384-dim vectors, no API cost, no GPU needed</td>
</tr>
<tr>
<td>🗃️ <b>Vector DB</b></td>
<td>ChromaDB (persistent)</td>
<td>0.5.3</td>
<td>In-process, no external server, cosine similarity built-in, perfect for POC</td>
</tr>
<tr>
<td>⚡ <b>Orchestration</b></td>
<td>LangGraph</td>
<td>0.2.14</td>
<td>Stateful typed pipeline, each node independently testable, observable graph execution</td>
</tr>
<tr>
<td>🌐 <b>Backend API</b></td>
<td>FastAPI + Uvicorn</td>
<td>0.115</td>
<td>Async Python REST, auto Swagger docs, Pydantic validation, production-grade performance</td>
</tr>
<tr>
<td>🎨 <b>Frontend</b></td>
<td>Streamlit</td>
<td>1.39</td>
<td>Rapid recruiter dashboard with live updates, dark theme, minimal frontend code</td>
</tr>
<tr>
<td>🐳 <b>Deployment</b></td>
<td>Docker + Compose</td>
<td>Latest</td>
<td>Single-command reproducible full-stack deployment with persistent ChromaDB volume</td>
</tr>
<tr>
<td>🔄 <b>CI/CD</b></td>
<td>GitHub Actions</td>
<td>—</td>
<td>Automated tests on every push — verifies imports, scoring logic, dataset integrity</td>
</tr>
<tr>
<td>📦 <b>Data</b></td>
<td>Python synthetic generator</td>
<td>—</td>
<td>300 realistic profiles with 20+ fields — skills, GitHub, career, activity, salary signals</td>
</tr>
</tbody>
</table>

</div>

---

## 🗂️ Candidate Data Schema

Each of the 300 synthetic candidates carries a rich, realistic profile:

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
  "experience": [{ "company": "Razorpay", "role": "ML Engineer", "duration_years": 3 }],
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

## 💡 RecruitMind AI vs The World

<div align="center">

| Dimension | Traditional ATS | RecruitMind AI |
|:---------:|:---------------:|:--------------:|
| JD Understanding | Keyword extraction | LLM semantic parsing + implicit detection |
| Candidate Matching | `if skill in resume` | Cosine similarity over 384-dim embeddings |
| Scoring | Binary pass/fail | 5-signal weighted composite |
| Ranking | Date applied | Multi-dimensional AI score |
| Explanation | None | Per-candidate LLM recruiter note |
| Diversity | None | Built-in 0.95× re-ranker |
| Transparency | Black box | Full score breakdown per signal |
| Bias Detection | None | POST /bias-check with flagging |
| Comparison | None | Side-by-side via POST /compare |
| Offline Support | N/A | Rule-based fallback always works |

</div>

---

## 🗺️ Roadmap

<div align="center">

<table>
<tr><td>🔲</td><td><b>Resume PDF parsing</b></td><td>Extract skills from uploaded resumes using PyMuPDF + LLM</td></tr>
<tr><td>🔲</td><td><b>LinkedIn profile integration</b></td><td>Live candidate data via LinkedIn API for real-world deployment</td></tr>
<tr><td>🔲</td><td><b>Feedback loop</b></td><td>Recruiter marks hired/rejected → system learns and improves ranking over time</td></tr>
<tr><td>🔲</td><td><b>Multi-JD batch ranking</b></td><td>Rank candidates across multiple open roles simultaneously</td></tr>
<tr><td>🔲</td><td><b>Bias detection expansion</b></td><td>ML-based bias detection beyond keyword patterns</td></tr>
<tr><td>🔲</td><td><b>PostgreSQL + pgvector migration</b></td><td>Production-grade horizontal scaling from ChromaDB</td></tr>
</table>

</div>

---

## 📁 Key Files Reference

<div align="center">

| File | Role |
|:----:|:-----|
| `pipeline/ranker.py` | 🧠 LangGraph graph — the core brain of the entire system |
| `pipeline/scorer.py` | 📊 All 5 scoring functions + weighted composite calculator |
| `pipeline/jd_parser.py` | 🤖 Groq LLM + offline structured JD extraction |
| `pipeline/embedder.py` | 🔢 ChromaDB indexing + semantic search engine |
| `pipeline/explainer.py` | 💬 LLM + rule-based recruiter note generator |
| `api/main.py` | ⚡ FastAPI with 8 REST endpoints |
| `ui/app.py` | 🎨 Full Streamlit recruiter dashboard |
| `data/generate_candidates.py` | 👥 300-candidate synthetic dataset generator |
| `run.sh` | 🚀 One-command startup script |
| `docker-compose.yml` | 🐳 Full stack Docker orchestration |

</div>

---

## 🔑 Getting a Free Groq API Key

```
1. Visit   →  https://console.groq.com
2. Sign up    (free — no credit card required)
3. Go to   →  API Keys → Create API Key
4. Add to  →  .env as GROQ_API_KEY=your_key_here
```

> **No key?** RecruitMind AI automatically falls back to rule-based offline mode. All semantic search, multi-signal scoring, and ranking still works fully.

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

![Azure AI-900](https://img.shields.io/badge/Microsoft-Azure_AI--900-0078D4?style=flat-square&logo=microsoft&logoColor=white)
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

⭐ **If this project impressed you, please give it a star!** ⭐

</div>
READMEEOF
echo "Done — $(wc -l < /mnt/user-data/outputs/README.md) lines"
