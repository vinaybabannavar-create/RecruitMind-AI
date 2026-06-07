"""
pipeline/explainer.py
Generates human-readable reasoning for each ranked candidate using an LLM.
Falls back to rule-based explanation if LLM is unavailable.
"""

import os
import json
import re
from typing import Dict, Any, List


EXPLAIN_PROMPT = """You are an expert AI recruiter. Given a job description and a candidate profile, 
write a SHORT recruiter-style explanation (3-4 sentences) of why this candidate is ranked #{rank}.

Job Title: {job_title}
Required Skills: {required_skills}
Experience Required: {min_exp}+ years, Seniority: {seniority}

Candidate: {name}
Skills: {skills}
Experience: {years_exp} years ({candidate_seniority})
Score Breakdown: Semantic={semantic}, Skill Match={skill_match}, Career={career}, Activity={activity}

Write a professional, specific explanation covering:
1. What makes them a good/partial fit
2. Their standout strengths
3. Any gaps (if any)

Keep it under 80 words. Be direct and factual. No fluff."""


def explain_with_llm(candidate: Dict, parsed_jd: Dict, rank: int) -> str:
    """Generate explanation using Groq LLM."""
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    scores = candidate.get("score_breakdown", {})
    meta = candidate.get("metadata", {})

    prompt = EXPLAIN_PROMPT.format(
        rank=rank,
        job_title=parsed_jd.get("job_title", "Software Engineer"),
        required_skills=", ".join(parsed_jd.get("required_skills", [])[:6]),
        min_exp=parsed_jd.get("min_experience_years", 0),
        seniority=parsed_jd.get("seniority_level", "mid"),
        name=candidate.get("name", "Candidate"),
        skills=", ".join(meta.get("skills", [])[:8]),
        years_exp=meta.get("years_experience", 0),
        candidate_seniority=meta.get("seniority", ""),
        semantic=round(scores.get("semantic_similarity", 0) * 100),
        skill_match=round(scores.get("skill_match", 0) * 100),
        career=round(scores.get("career_growth", 0) * 100),
        activity=round(scores.get("activity", 0) * 100),
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()


def explain_rule_based(candidate: Dict, parsed_jd: Dict, rank: int) -> str:
    """Rule-based explanation fallback (no LLM needed)."""
    meta = candidate.get("metadata", {})
    scores = candidate.get("score_breakdown", {})

    name = candidate.get("name", "Candidate")
    years = meta.get("years_experience", 0)
    seniority = meta.get("seniority", "")
    skills = meta.get("skills", [])
    certs = meta.get("certifications", [])
    prs = meta.get("open_source_prs", 0)

    required_skills = parsed_jd.get("required_skills", [])
    matched = [s for s in required_skills if s.lower() in [sk.lower() for sk in skills]]
    missing = [s for s in required_skills if s.lower() not in [sk.lower() for sk in skills]]

    skill_pct = round(scores.get("skill_match", 0) * 100)
    sem_pct = round(scores.get("semantic_similarity", 0) * 100)
    career_pct = round(scores.get("career_growth", 0) * 100)

    parts = []
    parts.append(f"**{name}** is ranked #{rank} with a composite score of {round(candidate.get('composite_score', 0) * 100)}%.")

    if matched:
        parts.append(f"Strong skill alignment ({skill_pct}%): matches on {', '.join(matched[:4])}.")
    else:
        parts.append(f"Skill match score: {skill_pct}%.")

    if years > 0:
        parts.append(f"{years} years of experience as a {seniority} engineer.")

    if prs > 5:
        parts.append(f"Active open source contributor ({prs} PRs).")

    if certs:
        parts.append(f"Certified: {', '.join(certs[:2])}.")

    if missing:
        parts.append(f"Gaps: missing {', '.join(missing[:3])}.")

    return " ".join(parts)


def add_explanations(
    shortlist: List[Dict],
    parsed_jd: Dict,
    use_llm: bool = None
) -> List[Dict]:
    """
    Add 'explanation' field to each candidate in the shortlist.
    Automatically detects whether to use LLM or rule-based.
    """
    if use_llm is None:
        use_llm = bool(os.getenv("GROQ_API_KEY"))

    enriched = []
    for candidate in shortlist:
        rank = candidate.get("rank", 0)
        try:
            if use_llm:
                explanation = explain_with_llm(candidate, parsed_jd, rank)
            else:
                explanation = explain_rule_based(candidate, parsed_jd, rank)
        except Exception as e:
            explanation = explain_rule_based(candidate, parsed_jd, rank)

        candidate["explanation"] = explanation
        enriched.append(candidate)

    return enriched


if __name__ == "__main__":
    sample_candidate = {
        "rank": 1,
        "name": "Aditya Sharma",
        "composite_score": 0.82,
        "score_breakdown": {
            "semantic_similarity": 0.88,
            "skill_match": 0.90,
            "career_growth": 0.75,
            "activity": 0.65,
            "experience_fit": 0.80,
        },
        "metadata": {
            "years_experience": 5,
            "seniority": "senior",
            "skills": ["Python", "FastAPI", "LangChain", "Docker", "Machine Learning", "PostgreSQL"],
            "certifications": ["AWS Solutions Architect"],
            "open_source_prs": 12,
            "email": "aditya.sharma@email.com",
            "summary": "Senior ML engineer with 5 years experience."
        }
    }

    sample_jd = {
        "job_title": "Senior ML Engineer",
        "required_skills": ["Python", "FastAPI", "LangChain", "Docker", "Machine Learning"],
        "min_experience_years": 4,
        "seniority_level": "senior",
    }

    result = add_explanations([sample_candidate], sample_jd)
    print(result[0]["explanation"])
