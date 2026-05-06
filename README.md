# Resume Screening

## Overview
A simple AI-style resume screening system that analyzes resumes and matches them with required job skills.

---

## Features
- Extract text from resume files
- Detect matching technical skills
- Calculate resume match score
- Simple NLP-based screening logic

---

## Files
- `extract_text.py` → extracts and cleans resume text
- `skill_match.py` → performs skill matching and scoring

---

## Required Skills

```text
python
machine learning
sql
data analysis
```

---

## Usage

### Run skill matching

```bash
python skill_match.py
```

---

## Example Resume

```text
Python developer with machine learning and SQL experience.
Worked on data analysis projects.
```

---

## Example Output

```python
{
  'matched_skills': [
    'python',
    'machine learning',
    'sql',
    'data analysis'
  ],
  'score': 100.0
}
```

---

## Use Case
- AI recruitment systems
- Resume ranking platforms
- HR automation tools
- Candidate screening systems

---

## Future Improvements
- PDF resume support
- TF-IDF based matching
- Resume ranking system
- Web API integration
- Deep learning based scoring