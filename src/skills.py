skills_db = [
    # Programming & Scripting
    "Python", "Java", "C++", "C#", "JavaScript", "MATLAB", "SQL", "HTML", "CSS", "Ruby", "Go",

    # Data & Machine Learning
    "Machine Learning", "Deep Learning", "Data Analysis", "Data Science", "TensorFlow", "PyTorch",
    "Scikit-learn", "Keras", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Power BI", "Tableau","UIUX",

    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "CI/CD", "Git", "Linux",

    # Other Tools & Software
    "Excel", "Word", "PowerPoint", "Jupyter Notebook", "Google Analytics", "ERP", "CRM",

    # Soft skills / business
    "Communication", "Teamwork", "Leadership", "Problem Solving", "Project Management",
    "Agile", "Scrum", "Time Management"
]

def extract_skills(text):
    text_lower = text.lower()
    return [s for s in skills_db if s in text]