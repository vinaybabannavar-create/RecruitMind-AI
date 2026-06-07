"""
pipeline/scorer.py
Multi-signal scoring engine.
Combines semantic similarity, skill match, career signals, and activity signals
into a single composite score for each candidate.
"""

import json
from typing import Dict, Any, List


WEIGHTS = {
    "semantic":       0.35,   # Embedding cosine similarity to JD
    "skill_match":    0.30,   # Direct skill overlap score
    "career_growth":  0.15,   # Career progression quality
    "activity":       0.10,   # GitHub / LeetCode / hackathons
    "experience_fit": 0.10,   # How well experience years fit JD requirement
}


def skill_match_score(candidate_skills: List[str], required_skills: List[str], nice_skills: List[str]) -> float:
    """Score based on skill overlap with JD requirements."""
    if not required_skills:
        return 0.5

    cand_lower = {s.lower() for s in candidate_skills}
    req_lower = [s.lower() for s in required_skills]
    nice_lower = [s.lower() for s in nice_skills]

    # Required skills hit rate (weighted more)
    req_hits = sum(1 for s in req_lower if s in cand_lower)
    req_score = req_hits / len(req_lower) if req_lower else 0.0

    # Nice-to-have bonus
    nice_hits = sum(1 for s in nice_lower if s in cand_lower)
    nice_bonus = (nice_hits / len(nice_lower) * 0.2) if nice_lower else 0.0

    return min(1.0, round(req_score * 0.8 + nice_bonus, 4))


def experience_fit_score(candidate_years: int, min_exp: int, max_exp) -> float:
    """Score how well experience years fit the JD range."""
    if max_exp is None:
        max_exp = min_exp + 5

    if candidate_years < min_exp:
        # Under-experienced: linear penalty
        gap = min_exp - candidate_years
        return max(0.0, round(1.0 - (gap * 0.25), 4))
    elif candidate_years > max_exp:
        # Over-experienced: mild penalty
        gap = candidate_years - max_exp
        return max(0.5, round(1.0 - (gap * 0.08), 4))
    else:
        return 1.0


def career_growth_score(candidate: Dict[str, Any]) -> float:
    """Score based on career trajectory signals."""
    career = candidate.get("career_signals", {})

    raw_growth = career.get("career_growth_score", 0.5)
    promotions = career.get("promotions", 0)
    avg_tenure = career.get("avg_tenure_years", 1.0)

    # Tenure stability: 1-3 years avg is ideal
    if avg_tenure < 0.5:
        tenure_score = 0.3  # too much job hopping
    elif avg_tenure <= 3:
        tenure_score = 1.0
    elif avg_tenure <= 5:
        tenure_score = 0.8
    else:
        tenure_score = 0.7

    # Promotions bonus
    promo_bonus = min(0.2, promotions * 0.07)

    final = round((raw_growth * 0.6) + (tenure_score * 0.3) + promo_bonus, 4)
    return min(1.0, final)


def activity_score(candidate: Dict[str, Any]) -> float:
    """Score based on GitHub, LeetCode, hackathon activity."""
    github = candidate.get("github", {})
    activity = candidate.get("activity_signals", {})

    # GitHub signal (contributions, open source PRs)
    contribs = github.get("contributions_last_year", 0)
    prs = github.get("open_source_prs", 0)
    github_base = github.get("github_score", 0.5)

    contrib_score = min(1.0, contribs / 400)
    pr_score = min(1.0, prs / 20)
    github_final = (github_base * 0.4) + (contrib_score * 0.4) + (pr_score * 0.2)

    # LeetCode
    lc = activity.get("leetcode_solved", 0)
    lc_score = min(1.0, lc / 200)

    # Hackathons
    hacks = activity.get("hackathon_participations", 0)
    hack_score = min(1.0, hacks / 5)

    # Recency penalty
    days_inactive = activity.get("last_active_days_ago", 30)
    if days_inactive > 120:
        recency_mult = 0.7
    elif days_inactive > 60:
        recency_mult = 0.85
    else:
        recency_mult = 1.0

    final = round((github_final * 0.5 + lc_score * 0.3 + hack_score * 0.2) * recency_mult, 4)
    return min(1.0, final)


def seniority_fit(candidate_seniority: str, jd_seniority: str) -> float:
    """Bonus/penalty for seniority match."""
    levels = {"fresher": 0, "junior": 1, "mid": 2, "senior": 3, "lead": 4}
    cand_level = levels.get(candidate_seniority, 1)
    jd_level = levels.get(jd_seniority, 1)
    diff = abs(cand_level - jd_level)
    if diff == 0:
        return 1.0
    elif diff == 1:
        return 0.8
    elif diff == 2:
        return 0.5
    else:
        return 0.2


def score_candidate(
    candidate: Dict[str, Any],
    parsed_jd: Dict[str, Any],
    semantic_score: float
) -> Dict[str, Any]:
    """
    Compute composite score for a single candidate against a parsed JD.
    Returns a dict with all sub-scores and final composite score.
    """
    candidate_skills = candidate.get("skills", [])
    required_skills = parsed_jd.get("required_skills", [])
    nice_skills = parsed_jd.get("nice_to_have_skills", [])
    min_exp = parsed_jd.get("min_experience_years", 0)
    max_exp = parsed_jd.get("max_experience_years", None)
    jd_seniority = parsed_jd.get("seniority_level", "mid")

    skill_score = skill_match_score(candidate_skills, required_skills, nice_skills)
    exp_score = experience_fit_score(candidate.get("years_experience", 0), min_exp, max_exp)
    career_score = career_growth_score(candidate)
    act_score = activity_score(candidate)
    sen_fit = seniority_fit(candidate.get("seniority", "mid"), jd_seniority)

    # Apply seniority fit as a multiplier on experience score
    adjusted_exp_score = round(exp_score * sen_fit, 4)

    composite = round(
        semantic_score * WEIGHTS["semantic"] +
        skill_score * WEIGHTS["skill_match"] +
        career_score * WEIGHTS["career_growth"] +
        act_score * WEIGHTS["activity"] +
        adjusted_exp_score * WEIGHTS["experience_fit"],
        4
    )

    return {
        "candidate_id": candidate.get("id"),
        "name": candidate.get("name"),
        "scores": {
            "composite": composite,
            "semantic": round(semantic_score, 4),
            "skill_match": skill_score,
            "career_growth": career_score,
            "activity": act_score,
            "experience_fit": adjusted_exp_score,
        },
        "metadata": {
            "years_experience": candidate.get("years_experience", 0),
            "seniority": candidate.get("seniority", ""),
            "role_type": candidate.get("role_type", ""),
            "location": candidate.get("location", ""),
            "skills": candidate_skills,
            "github_repos": candidate.get("github", {}).get("repos", 0),
            "open_source_prs": candidate.get("github", {}).get("open_source_prs", 0),
            "certifications": candidate.get("certifications", []),
            "expected_salary_lpa": candidate.get("expected_salary_lpa", 0),
            "notice_period_days": candidate.get("notice_period_days", 0),
            "email": candidate.get("email", ""),
            "summary": candidate.get("summary", ""),
        }
    }


def score_all_candidates(
    candidates: List[Dict[str, Any]],
    parsed_jd: Dict[str, Any],
    semantic_results: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Score all candidates and return sorted list by composite score.

    candidates: full candidate profiles (from candidates.json)
    parsed_jd: structured JD from jd_parser
    semantic_results: list from embedder.search_candidates (has semantic_score per candidate)
    """
    # Build lookup for semantic scores
    semantic_map = {r["id"]: r["semantic_score"] for r in semantic_results}

    # Build lookup for candidate profiles by id
    candidate_map = {c["id"]: c for c in candidates}

    scored = []
    for result in semantic_results:
        cid = result["id"]
        candidate = candidate_map.get(cid)
        if not candidate:
            continue
        sem_score = semantic_map.get(cid, 0.0)
        scored.append(score_candidate(candidate, parsed_jd, sem_score))

    # Sort descending by composite score
    scored.sort(key=lambda x: x["scores"]["composite"], reverse=True)
    return scored


if __name__ == "__main__":
    import json

    with open("data/candidates.json") as f:
        candidates = json.load(f)

    sample_jd = {
        "job_title": "Senior ML Engineer",
        "required_skills": ["Python","Machine Learning","FastAPI","Docker","LangChain"],
        "nice_to_have_skills": ["RAG","Kubernetes","AWS"],
        "min_experience_years": 3,
        "max_experience_years": 7,
        "seniority_level": "senior",
        "role_type": "ml",
        "summary": "Looking for a senior ML engineer to build AI pipelines."
    }

    # Simulate semantic scores
    fake_semantic = [{"id": c["id"], "semantic_score": 0.7} for c in candidates[:10]]

    results = score_all_candidates(candidates, sample_jd, fake_semantic)
    for r in results[:5]:
        print(f"{r['name']} | composite={r['scores']['composite']} | skills={r['metadata']['skills'][:3]}")
