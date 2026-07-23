"""
pipeline/jd_parser.py
Parses a raw Job Description using an LLM into structured requirements.
"""

import os
import json
import re
from groq import Groq

def get_llm_client():
    """Returns Groq client. Set GROQ_API_KEY in .env"""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set. Add it to your .env file.")
    return Groq(api_key=api_key)


PARSE_PROMPT = """You are an expert technical recruiter AI. 
Given a raw job description, extract the following into a JSON object:

{{
  "job_title": "string",
  "required_skills": ["list of must-have skills"],
  "nice_to_have_skills": ["list of optional skills"],
  "min_experience_years": number,
  "max_experience_years": number or null,
  "seniority_level": "fresher|junior|mid|senior|lead",
  "role_type": "ml|ai|backend|fullstack|devops|data|other",
  "education_requirement": "string or null",
  "key_responsibilities": ["top 3-5 responsibilities as short phrases"],
  "culture_signals": ["keywords hinting at team culture, work style"],
  "implicit_expectations": ["things not explicitly stated but clearly expected"],
  "location": "string or Remote",
  "summary": "2 sentence summary of the ideal candidate"
}}

Job Description:
{jd_text}

Respond ONLY with valid JSON. No markdown, no explanation."""


def parse_jd(jd_text: str) -> dict:
    """
    Parse a raw job description string into structured requirements.
    Returns a dict with all extracted fields.
    """
    client = get_llm_client()

    prompt = PARSE_PROMPT.format(jd_text=jd_text.strip())

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=800,
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown code fences if present
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"```$", "", raw)
    raw = raw.strip()

    parsed = json.loads(raw)
    return parsed


def parse_jd_offline(jd_text: str) -> dict:
    """
    Offline fallback: extract JD info using simple heuristics.
    Used when no LLM API key is available (demo mode).
    """
    jd_lower = jd_text.lower()

    skill_keywords = [
        "Python","FastAPI","Flask","Django","React","Node.js","JavaScript",
        "TypeScript","Docker","Kubernetes","AWS","GCP","Azure","SQL","MongoDB",
        "PostgreSQL","Redis","Machine Learning","Deep Learning","TensorFlow",
        "PyTorch","LangChain","RAG","LLM","NLP","Scikit-learn","Pandas","NumPy",
        "CI/CD","Jenkins","GitHub Actions","Microservices","REST API","GraphQL",
        "Go","Java","Spring Boot","Spark","Airflow","Kafka","Linux","Git","Agile"
    ]

    found_skills = [s for s in skill_keywords if s.lower() in jd_lower]

    exp_match = re.search(r"(\d+)\+?\s*years?", jd_text, re.IGNORECASE)
    min_exp = int(exp_match.group(1)) if exp_match else 0

    seniority = "fresher"
    if "senior" in jd_lower or "lead" in jd_lower:
        seniority = "senior"
    elif "mid" in jd_lower or "3+" in jd_text or "4+" in jd_text:
        seniority = "mid"
    elif "junior" in jd_lower or "1+" in jd_text or "2+" in jd_text:
        seniority = "junior"

    role_type = "backend"
    if any(k in jd_lower for k in ["machine learning","ml","ai","deep learning","llm","nlp"]):
        role_type = "ml"
    elif any(k in jd_lower for k in ["fullstack","full stack","full-stack","react","vue"]):
        role_type = "fullstack"
    elif any(k in jd_lower for k in ["devops","kubernetes","docker","ci/cd","cloud"]):
        role_type = "devops"
    elif any(k in jd_lower for k in ["data engineer","spark","airflow","etl","pipeline"]):
        role_type = "data"

    return {
        "job_title": "Software Engineer",
        "required_skills": found_skills[:8],
        "nice_to_have_skills": found_skills[8:12],
        "min_experience_years": min_exp,
        "max_experience_years": None,
        "seniority_level": seniority,
        "role_type": role_type,
        "education_requirement": None,
        "key_responsibilities": ["Build and maintain software systems","Collaborate with team","Write clean code"],
        "culture_signals": ["collaborative","fast-paced"],
        "implicit_expectations": ["Good communication","Self-motivated"],
        "location": "Bengaluru",
        "summary": f"Looking for a {seniority} {role_type} engineer with skills in {', '.join(found_skills[:3])}."
    }


if __name__ == "__main__":
    sample_jd = """
    We are looking for a Senior Python Developer to join our AI team in Bengaluru.

    Requirements:
    - 4+ years of experience in Python
    - Strong knowledge of FastAPI, REST APIs, and microservices
    - Experience with Machine Learning pipelines and LangChain or LlamaIndex
    - Familiarity with Docker and Kubernetes
    - Experience with PostgreSQL and Redis
    - Good understanding of system design

    Nice to have:
    - Experience with RAG pipelines
    - Knowledge of AWS or GCP
    - Open source contributions

    You will be responsible for building AI-powered backend services, 
    collaborating with the ML team, and maintaining production systems.
    """

    use_llm = os.getenv("GROQ_API_KEY") is not None
    if use_llm:
        result = parse_jd(sample_jd)
    else:
        result = parse_jd_offline(sample_jd)

    print(json.dumps(result, indent=2))
