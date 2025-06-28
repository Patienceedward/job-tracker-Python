import re

def extract_keywords(text):
    words = re.findall(r"\b\w+\b", text.lower())
    stopwords = {"the", "and", "a", "of", "to", "in", "for", "with", "on", "is", "as", "by"}
    return set(words) - stopwords

def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return ""

def compare_keywords(job_file, resume_file):
    job_text = read_file(job_file)
    resume_text = read_file(resume_file)

    job_keywords = extract_keywords(job_text)
    resume_keywords = extract_keywords(resume_text)

    if not job_keywords:
        return 0

    match = job_keywords & resume_keywords
    match_percent = (len(match) / len(job_keywords)) * 100
    return round(match_percent, 2)
