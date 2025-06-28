import pdfplumber # type: ignore
import re

def extract_keywords(text):
    words = re.findall(r"\b\w+\b", text.lower())
    stopwords = {"the", "and", "a", "of", "to", "in", "for", "with", "on", "is", "as", "by"}
    return set(words) - stopwords

def read_pdf(file_obj):  # ✅ updated to work with uploaded files
    try:
        with pdfplumber.open(file_obj) as pdf:
            return ''.join(page.extract_text() or '' for page in pdf.pages)
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ""


def compare_keywords(job_file, resume_file):
    job_text = read_pdf(job_file)
    resume_text = read_pdf(resume_file)

    job_keywords = extract_keywords(job_text)
    resume_keywords = extract_keywords(resume_text)

    if not job_keywords:
        return 0

    match = job_keywords & resume_keywords
    match_percent = (len(match) / len(job_keywords)) * 100
    return round(match_percent, 2)
