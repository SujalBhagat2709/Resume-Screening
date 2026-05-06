from extract_text import extract_text

required_skills = [
    "python",
    "machine learning",
    "sql",
    "data analysis"
]

def match_skills(resume_path):
    
    text = extract_text(resume_path).lower()
    
    matched = []
    
    for skill in required_skills:
        if skill in text:
            matched.append(skill)
    
    score = len(matched) / len(required_skills) * 100
    
    return {
        "matched_skills": matched,
        "score": score
    }


if __name__ == "__main__":
    
    result = match_skills("resume.txt")
    
    print(result)