import streamlit as st
from matcher import extract_keywords, read_pdf

st.set_page_config(page_title="📄 Resume Matcher", layout="centered")
st.title("📄 Resume vs Job Match")
st.markdown("Upload your resume and job description as PDFs, or paste text.")

# File upload section
job_pdf = st.file_uploader("Upload Job Description PDF", type=["pdf"])
resume_pdf = st.file_uploader("Upload Resume PDF", type=["pdf"])

# Or paste text manually
st.markdown("**OR paste text manually below:**")
job_text = st.text_area("Paste Job Description")
resume_text = st.text_area("Paste Resume")

if st.button("Compare"):
    if job_pdf and resume_pdf:
        job_content = read_pdf(job_pdf)
        resume_content = read_pdf(resume_pdf)
    elif job_text and resume_text:
        job_content = job_text
        resume_content = resume_text
    else:
        st.warning("⚠️ Please upload or paste both documents to compare.")
        st.stop()

    job_keywords = extract_keywords(job_content)
    resume_keywords = extract_keywords(resume_content)

    matched = job_keywords & resume_keywords
    score = round(len(matched) / len(job_keywords) * 100, 2) if job_keywords else 0

    st.success(f"✅ Match Score: {score}%")
    if matched:
        st.markdown(f"**Matched Keywords:** {', '.join(sorted(matched))}")
    else:
        st.markdown("😬 No matching keywords found.")
