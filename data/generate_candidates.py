"""
generate_candidates.py
Generates 100 synthetic candidate profiles and saves to candidates.json
Run: python data/generate_candidates.py
"""

import json
import random
from datetime import datetime, timedelta

random.seed(42)

FIRST_NAMES = [
    "Aditya","Priya","Rahul","Sneha","Vikram","Ananya","Rohan","Divya",
    "Karan","Meera","Arjun","Pooja","Nikhil","Shreya","Amit","Neha",
    "Siddharth","Kavya","Ravi","Ishaan","James","Sarah","Michael","Emily",
    "David","Jessica","Daniel","Ashley","Chris","Amanda","John","Megan",
    "Kevin","Lauren","Brian","Stephanie","Jason","Nicole","Ryan","Heather"
]

LAST_NAMES = [
    "Sharma","Patel","Kumar","Singh","Gupta","Reddy","Nair","Mehta",
    "Joshi","Verma","Smith","Johnson","Williams","Brown","Jones","Davis",
    "Miller","Wilson","Moore","Taylor","Anderson","Thomas","Jackson","White",
    "Harris","Martin","Thompson","Garcia","Martinez","Robinson"
]

SKILLS_POOL = {
    "python": ["Python","FastAPI","Flask","Django","NumPy","Pandas","Scikit-learn"],
    "ml": ["Machine Learning","Deep Learning","TensorFlow","PyTorch","Keras","NLP","LangChain","RAG","LLM","Hugging Face"],
    "backend": ["Node.js","Go","Java","Spring Boot","REST API","GraphQL","Microservices","PostgreSQL","MySQL","MongoDB","Redis"],
    "frontend": ["React","Vue.js","Angular","TypeScript","JavaScript","Tailwind CSS","Next.js"],
    "devops": ["Docker","Kubernetes","CI/CD","Jenkins","GitHub Actions","AWS","GCP","Azure","Terraform","Linux"],
    "data": ["SQL","Spark","Hadoop","Airflow","dbt","Snowflake","BigQuery","Power BI","Tableau"],
    "other": ["Git","Agile","Scrum","REST","System Design","Problem Solving"]
}

COMPANIES = [
    "Google","Microsoft","Amazon","Flipkart","Infosys","TCS","Wipro","Razorpay",
    "Swiggy","Zomato","CRED","Meesho","PhonePe","Paytm","Ola","Byju's",
    "Freshworks","Zoho","HCL","Cognizant","Accenture","Capgemini","IBM","Oracle",
    "Startup XYZ","DataCorp","AIVentures","TechSolutions","CloudBase","DevHouse"
]

COLLEGES = [
    "IIT Bombay","IIT Delhi","IIT Madras","IIT Bangalore","NIT Trichy",
    "NIT Warangal","BITS Pilani","VIT Vellore","Anna University","IIIT Hyderabad",
    "Delhi University","Mumbai University","Pune University","Bangalore University",
    "Manipal Institute","SRM University","Amity University","Chandigarh University"
]

DEGREES = ["B.Tech Computer Science","B.Tech Information Technology",
           "M.Tech Computer Science","MCA","B.E. Electronics","B.Sc Computer Science"]

ROLES = [
    "Software Engineer","Senior Software Engineer","Backend Developer",
    "Full Stack Developer","ML Engineer","Data Scientist","DevOps Engineer",
    "Python Developer","AI/ML Engineer","Data Engineer","Cloud Engineer",
    "Frontend Developer","Platform Engineer","Research Engineer"
]

def random_date(years_back_min, years_back_max):
    days = random.randint(years_back_min * 365, years_back_max * 365)
    return (datetime.now() - timedelta(days=days)).strftime("%Y-%m")

def pick_skills(role_type, count):
    selected = []
    if role_type in ["ml", "ai"]:
        selected += random.sample(SKILLS_POOL["python"], random.randint(3, 5))
        selected += random.sample(SKILLS_POOL["ml"], random.randint(3, 6))
        selected += random.sample(SKILLS_POOL["other"], random.randint(1, 3))
    elif role_type == "backend":
        selected += random.sample(SKILLS_POOL["python"], random.randint(2, 4))
        selected += random.sample(SKILLS_POOL["backend"], random.randint(3, 5))
        selected += random.sample(SKILLS_POOL["devops"], random.randint(1, 3))
        selected += random.sample(SKILLS_POOL["other"], random.randint(1, 2))
    elif role_type == "fullstack":
        selected += random.sample(SKILLS_POOL["frontend"], random.randint(2, 4))
        selected += random.sample(SKILLS_POOL["backend"], random.randint(2, 4))
        selected += random.sample(SKILLS_POOL["python"], random.randint(1, 3))
        selected += random.sample(SKILLS_POOL["other"], random.randint(1, 2))
    elif role_type == "devops":
        selected += random.sample(SKILLS_POOL["devops"], random.randint(4, 6))
        selected += random.sample(SKILLS_POOL["backend"], random.randint(1, 3))
        selected += random.sample(SKILLS_POOL["other"], random.randint(1, 2))
    elif role_type == "data":
        selected += random.sample(SKILLS_POOL["data"], random.randint(3, 5))
        selected += random.sample(SKILLS_POOL["python"], random.randint(2, 4))
        selected += random.sample(SKILLS_POOL["ml"], random.randint(1, 3))
    return list(set(selected))[:count]

def generate_experience(years_exp):
    jobs = []
    current_year = datetime.now().year
    end_year = current_year
    remaining = years_exp

    while remaining > 0:
        duration = random.randint(1, min(3, remaining))
        start_year = end_year - duration
        jobs.append({
            "company": random.choice(COMPANIES),
            "role": random.choice(ROLES),
            "start": f"{start_year}-{random.randint(1,12):02d}",
            "end": f"{end_year}-{random.randint(1,12):02d}" if end_year < current_year else "Present",
            "duration_years": duration
        })
        end_year = start_year
        remaining -= duration

    return jobs

def generate_candidate(cid):
    role_types = ["ml", "ai", "backend", "fullstack", "devops", "data"]
    role_type = random.choice(role_types)

    years_exp = random.randint(0, 10)
    seniority = "fresher" if years_exp == 0 else ("junior" if years_exp <= 2 else ("mid" if years_exp <= 5 else "senior"))

    name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    skills = pick_skills(role_type, random.randint(6, 14))

    github_score = round(random.uniform(0.1, 1.0), 2)
    activity_score = round(random.uniform(0.1, 1.0), 2)
    career_growth = round(random.uniform(0.2, 1.0), 2)

    certifications = []
    cert_pool = ["AWS Solutions Architect","Google Cloud Professional","Azure AZ-900",
                 "TensorFlow Developer Certificate","Coursera ML Specialization",
                 "Deep Learning Specialization","Docker Certified","Kubernetes CKA",
                 "Microsoft AI-900","Cisco CCNA","NPTEL Python","Kaggle Competition Winner"]
    if random.random() > 0.4:
        certifications = random.sample(cert_pool, random.randint(1, 3))

    open_source_contributions = random.randint(0, 50)
    github_repos = random.randint(0, 40)
    leetcode_problems = random.randint(0, 400)

    summary_templates = [
        f"{seniority.capitalize()} {role_type.upper()} engineer with {years_exp} years of experience in {', '.join(skills[:3])}.",
        f"Passionate about {role_type} development. Strong background in {', '.join(skills[:4])} with hands-on project experience.",
        f"Results-driven developer specializing in {', '.join(skills[:3])}. {years_exp} years building scalable systems.",
        f"Detail-oriented engineer with expertise in {', '.join(skills[:4])}. Love solving complex problems.",
    ]

    return {
        "id": f"CAND_{cid:04d}",
        "name": name,
        "email": f"{name.lower().replace(' ', '.')}@email.com",
        "location": random.choice(["Bengaluru","Mumbai","Hyderabad","Pune","Chennai","Delhi","Remote"]),
        "summary": random.choice(summary_templates),
        "years_experience": years_exp,
        "seniority": seniority,
        "role_type": role_type,
        "skills": skills,
        "education": {
            "degree": random.choice(DEGREES),
            "college": random.choice(COLLEGES),
            "graduation_year": random.randint(2010, 2026),
            "cgpa": round(random.uniform(6.0, 10.0), 1)
        },
        "experience": generate_experience(years_exp) if years_exp > 0 else [],
        "certifications": certifications,
        "github": {
            "username": name.lower().replace(" ", "_"),
            "repos": github_repos,
            "contributions_last_year": random.randint(0, 800),
            "open_source_prs": open_source_contributions,
            "github_score": github_score
        },
        "activity_signals": {
            "leetcode_solved": leetcode_problems,
            "hackathon_participations": random.randint(0, 8),
            "blog_posts": random.randint(0, 15),
            "linkedin_activity_score": activity_score,
            "last_active_days_ago": random.randint(1, 180)
        },
        "career_signals": {
            "career_growth_score": career_growth,
            "avg_tenure_years": round(years_exp / max(len(generate_experience(years_exp)), 1), 1) if years_exp > 0 else 0,
            "promotions": random.randint(0, 3),
            "companies_worked": max(1, years_exp // 2)
        },
        "preferred_roles": [random.choice(ROLES) for _ in range(random.randint(1, 3))],
        "notice_period_days": random.choice([0, 15, 30, 60, 90]),
        "expected_salary_lpa": round(random.uniform(3, 50), 1),
        "open_to_remote": random.choice([True, False])
    }

def main():
    candidates = [generate_candidate(i) for i in range(1, 301)]
    output_path = "data/candidates.json"
    with open(output_path, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"Generated {len(candidates)} candidates -> {output_path}")

if __name__ == "__main__":
    main()
