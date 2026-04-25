# AI-IT-Recruitment-System
**Utilizing Artificial Intelligence in IT Recruitment: Enhancing Efficiency and Effectiveness**

## 🚀 Overview
This project is an AI-powered recruitment platform designed to automate the screening and ranking of IT candidates. It uses Natural Language Processing (NLP) to match resumes with job descriptions using TF-IDF and Cosine Similarity.

## ✨ Key Features
* **Automated Resume Parsing:** Extracts text from PDF and DOCX files.
* **AI Matching Engine:** Ranks candidates based on skill relevancy.
* **Smart Dashboard:** Visual representation of candidate scores.
* **Efficiency:** Reduces screening time by up to 90%.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Libraries:** NLTK, Spacy, Scikit-Learn, PyPDF2
* **Database:** MySQL / MongoDB
* **Framework:** Flask/Django (for Web Interface)

## 📊 Methodology
The system calculates the **Cosine Similarity** between the Job Description (JD) and Resume vectors:
$$Score = \frac{A \cdot B}{\|A\| \|B\|}$$
