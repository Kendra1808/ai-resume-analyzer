# AI Resume Analyzer & Job Matching System

## Overview
An AI-powered Resume Analyzer and Job Recommendation System developed using Machine Learning, Natural Language Processing (NLP) and Streamlit.
The system analyzes uploaded resumes, predicts suitable job categories, extracts technical skills and recommends relevant IT-related job roles.

## Features
- Resume PDF Upload
- Resume Text Extraction
- Resume Classification using Machine Learning
- Skill Extraction
- Resume Score Calculation
- Job Recommendations
- Cosine Similarity Matching
- Interactive Streamlit User Interface
- NLP-based Text Preprocessing
- Streamlit web application

## Technologies
- Python
- Scikit-learn
- spaCy
- NLP (TF-IDF / Sentence Transformers)
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Sample Resume
## Due to PDF parsing limitations in GitHub and Streamlit, sample resume is provided in text format.
- copy and paste the sample resume texts.
- upload in pdf format.

## How to Run
1. Clone Repository:
   git clone <github-link>
   cd ai-resume-analyzer

2. Install dependencies:
   pip install -r requirements.txt

3. Download spaCy Model:
   python -m spacy download en_core_web_sm

4. Run Application:
   streamlit run app.py