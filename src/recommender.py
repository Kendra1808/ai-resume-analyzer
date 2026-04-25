from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(resume_vec, job_vecs, jobs, top_k=5):
    sim = cosine_similarity(resume_vec, job_vecs)
    idx = sim[0].argsort()[-top_k:][::-1]
    return [(jobs.iloc[i]["Title"], sim[0][i]) for i in idx]