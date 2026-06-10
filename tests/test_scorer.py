"""
tests/test_scorer.py
Unit tests for pipeline/scorer.py scoring logic.
"""

import pytest
from pipeline.scorer import (
    skill_match_score,
    experience_fit_score,
    career_growth_score,
    activity_score,
    seniority_fit,
    score_candidate,
    WEIGHTS
)

def test_skill_match_score():
    # Test with empty required skills
    assert skill_match_score(["Python"], [], ["RAG"]) == 0.5

    # Test exact match of required skills
    candidate_skills = ["Python", "FastAPI", "Docker"]
    required_skills = ["Python", "FastAPI"]
    nice_skills = ["Docker", "Kubernetes"]
    # 2/2 required skills matched = 1.0. Weighted by 0.8 -> 0.8
    # 1/2 nice skills matched = 0.5. Nice bonus -> 0.5 * 0.2 = 0.1
    # expected: min(1.0, 0.8 + 0.1) = 0.9
    assert skill_match_score(candidate_skills, required_skills, nice_skills) == 0.9

    # Test all matches
    candidate_skills_all = ["Python", "FastAPI", "Docker", "Kubernetes"]
    # 2/2 required (1.0 * 0.8 = 0.8) + 2/2 nice (1.0 * 0.2 = 0.2) = 1.0
    assert skill_match_score(candidate_skills_all, required_skills, nice_skills) == 1.0

    # Test case insensitivity
    candidate_caps = ["PYTHON", "fastapi"]
    assert skill_match_score(candidate_caps, required_skills, nice_skills) == 0.8

def test_experience_fit_score():
    # Perfect fit (between min and max)
    assert experience_fit_score(5, 3, 7) == 1.0
    assert experience_fit_score(3, 3, 7) == 1.0
    assert experience_fit_score(7, 3, 7) == 1.0

    # Under-experienced
    # gap = 3 - 2 = 1. Score: 1.0 - 0.25 = 0.75
    assert experience_fit_score(2, 3, 7) == 0.75
    # gap = 3 - 1 = 2. Score: 1.0 - 0.5 = 0.5
    assert experience_fit_score(1, 3, 7) == 0.5

    # Over-experienced
    # gap = 9 - 7 = 2. Score: 1.0 - 2 * 0.08 = 0.84
    assert experience_fit_score(9, 3, 7) == 0.84

    # Default max_exp when None
    # min_exp = 3. max_exp default is 3 + 5 = 8.
    # 5 is a perfect fit
    assert experience_fit_score(5, 3, None) == 1.0
    # 10 is over-experienced by 2. gap = 10 - 8 = 2. Score: 1.0 - 0.16 = 0.84
    assert experience_fit_score(10, 3, None) == 0.84

def test_career_growth_score():
    candidate_good = {
        "career_signals": {
            "career_growth_score": 0.8,
            "promotions": 2,
            "avg_tenure_years": 2.0
        }
    }
    # raw_growth (0.8 * 0.6 = 0.48) + tenure (1.0 * 0.3 = 0.3) + promo_bonus (2 * 0.07 = 0.14) = 0.92
    assert career_growth_score(candidate_good) == 0.92

    candidate_job_hopper = {
        "career_signals": {
            "career_growth_score": 0.5,
            "promotions": 0,
            "avg_tenure_years": 0.4
        }
    }
    # raw_growth (0.5 * 0.6 = 0.3) + tenure (0.3 * 0.3 = 0.09) + promo_bonus (0) = 0.39
    assert career_growth_score(candidate_job_hopper) == 0.39

def test_activity_score():
    candidate_active = {
        "github": {
            "contributions_last_year": 300,
            "open_source_prs": 10,
            "github_score": 0.8
        },
        "activity_signals": {
            "leetcode_solved": 150,
            "hackathon_participations": 3,
            "last_active_days_ago": 15
        }
    }
    # github_final: (0.8 * 0.4) + (300/400 * 0.4 = 0.3) + (10/20 * 0.2 = 0.1) = 0.72
    # lc_score: 150 / 200 = 0.75
    # hack_score: 3 / 5 = 0.6
    # recency_mult = 1.0 (since last_active_days_ago <= 60)
    # final = (0.72 * 0.5 + 0.75 * 0.3 + 0.6 * 0.2) * 1.0 = (0.36 + 0.225 + 0.12) * 1.0 = 0.705
    assert activity_score(candidate_active) == 0.705

    # Test recency penalty
    candidate_inactive = {
        "github": {
            "contributions_last_year": 100,
            "open_source_prs": 0,
            "github_score": 0.5
        },
        "activity_signals": {
            "leetcode_solved": 0,
            "hackathon_participations": 0,
            "last_active_days_ago": 150
        }
    }
    # github_final: 0.5 * 0.4 + 0.25 * 0.4 = 0.3
    # lc_score: 0.0
    # hack_score: 0.0
    # recency_mult: 0.7 (since > 120 days ago)
    # final: (0.3 * 0.5) * 0.7 = 0.15 * 0.7 = 0.105
    assert activity_score(candidate_inactive) == 0.105

def test_seniority_fit():
    assert seniority_fit("senior", "senior") == 1.0
    assert seniority_fit("senior", "lead") == 0.8
    assert seniority_fit("junior", "senior") == 0.5
    assert seniority_fit("fresher", "lead") == 0.2

def test_score_candidate():
    candidate = {
        "id": "CAND_TEST_99",
        "name": "Jane Doe",
        "skills": ["Python", "FastAPI", "Docker"],
        "years_experience": 5,
        "seniority": "senior",
        "career_signals": {
            "career_growth_score": 0.8,
            "promotions": 2,
            "avg_tenure_years": 2.0
        },
        "github": {
            "contributions_last_year": 300,
            "open_source_prs": 10,
            "github_score": 0.8
        },
        "activity_signals": {
            "leetcode_solved": 150,
            "hackathon_participations": 3,
            "last_active_days_ago": 15
        }
    }

    parsed_jd = {
        "required_skills": ["Python", "FastAPI"],
        "nice_to_have_skills": ["Docker", "Kubernetes"],
        "min_experience_years": 3,
        "max_experience_years": 7,
        "seniority_level": "senior"
    }

    result = score_candidate(candidate, parsed_jd, semantic_score=0.85)

    assert result["candidate_id"] == "CAND_TEST_99"
    assert result["name"] == "Jane Doe"
    assert "scores" in result
    assert result["scores"]["semantic"] == 0.85
    assert result["scores"]["skill_match"] == 0.9
    assert result["scores"]["experience_fit"] == 1.0 # 5 yrs exp, senior vs senior (fit=1.0)
    assert result["scores"]["career_growth"] == 0.92
    assert result["scores"]["activity"] == 0.705

    # Check composite calculation
    expected_composite = round(
        0.85 * WEIGHTS["semantic"] +
        0.9 * WEIGHTS["skill_match"] +
        0.92 * WEIGHTS["career_growth"] +
        0.705 * WEIGHTS["activity"] +
        1.0 * WEIGHTS["experience_fit"],
        4
    )
    assert result["scores"]["composite"] == expected_composite
