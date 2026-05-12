skills_db = [
    # Programming & Scripting
    "Python", "Java", "C++", "C#", "JavaScript", "MATLAB", "SQL", "HTML", "CSS", "Ruby", "Flutter", "React", "API", "Software"

    # Data & Machine Learning
    "Machine Learning", "Deep Learning", "Data Analysis", "Data Science", "Data Visualization", "TensorFlow", "PyTorch", "Cybersecurity",
    "Scikit-learn", "Keras", "Pandas", "NumPy", "Matplotlib", "Seaborn", "Power BI", "Tableau","UI" ,"UX", "Figma",
    "Wireframing", "Prototyping"

    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "CI/CD", "Git", "Linux",

    # Other Tools & Software
    "Microsoft", "Excel", "Word", "PowerPoint", "Jupyter Notebook", "Google" , "Analytics", "Analysis", 
    "ERP", "CRM", "Content", "Social", "AutoCAD",

    # Soft skills / business
    "Communication", "Teamwork", "Leadership", "Problem Solving", "Project Management", "Critical Thinking", "Creativity",
    "Agile", "Scrum", "Time Management", "Training", "HR",
]

def extract_skills(text):
    text_lower = text.lower()
    return [s for s in skills_db if s in text]