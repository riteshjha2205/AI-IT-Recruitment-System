import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(job_description, resumes):
    # Documents ko list mein daalein
    documents = [job_description] + resumes
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Cosine Similarity calculate karein (JD vs Resumes)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return scores[0]

# Demo Data
jd = "Looking for a Python Developer with experience in Flask, MySQL, and NLP."
resumes = [
    "I am a Python Developer specialized in Flask and Machine Learning.",
    "Experienced Java developer working on Spring Boot and Cloud.",
    "Python enthusiast with knowledge of SQL and Data Science."
]

print("Scanning Resumes...")
results = calculate_score(jd, resumes)

for i, score in enumerate(results):
    print(f"Candidate {i+1} Match Score: {round(score*100, 2)}%")
