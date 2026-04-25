import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from src.utils import pdf_to_text
from src.preprocessing import clean_text
from src.skills import extract_skills

# Page Config
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("AI Resume Analyzer & Job Recommender 📄")

# Load everything
@st.cache_resource
def load_model():
    return joblib.load("models/model.pkl"), joblib.load("models/tfidf.pkl")

@st.cache_data
def load_jobs():
    return pd.read_csv("data/Jobb_clean.csv")

# Precompute job vectors
model, tfidf = load_model()
jobs = load_jobs()

job_vectors = tfidf.transform(jobs["clean"])

# Upload file
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf"])

if uploaded_file:
    text = pdf_to_text(uploaded_file)
    clean = clean_text(text)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📄 Resume Preview")
        st.write(text[:1000])

# -------------------------
# Prediction
# -------------------------
    vec = tfidf.transform([clean])
    prediction = model.predict(vec)[0]

    with col2:
        st.subheader("🧠 Predicted Role")
        st.success(prediction)

    # -------------------------
    # Skills
    # -------------------------
        skills = extract_skills(text)
        st.subheader("🛠 Extracted Skills")
        st.write("Skills:", skills)

    # -------------------------
    # Resume score
    # -------------------------
        score = len(skills) * 5
        st.metric("📊 Resume Score", score)

    # -------------------------
    # Job recommendation
    # -------------------------
        similarity = cosine_similarity(vec, job_vectors)
        top_idx = similarity[0].argsort()[-5:][::-1]

        st.subheader("💼 Recommended Jobs")

        for i in top_idx:
            title = jobs["Title"].iloc[i]
            score_val = similarity[0][i]

            st.write(f"👉 {title}")
            st.progress(int(score_val * 100))
            st.write(f"Match Score: {score_val:.2f}")
        
            tips = [
            "Use bullet points for readability",
            "Quantify achievements (e.g., improved performance by 20%)",
            "Keep resume to 1–2 pages",
            "Include relevant keywords for ATS systems"
]

    st.subheader("📌 Resume Tips")
    for tip in tips:
        st.write(f"✔ {tip}")
        
    st.subheader("🎥 Learn More")

    st.video("https://youtu.be/R3abknwWX7k?si=qcm0v-2yskDp1B-D")

    st.subheader("📊 Conclusion")

    st.write(f"""
    This resume is most suitable for **{prediction}** roles.

    The system identified key strengths in:
    - {', '.join(skills)}

    Improvement areas include adding more measurable achievements and expanding technical skills.
    """)