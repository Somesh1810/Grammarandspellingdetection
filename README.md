#  Grammar & Spelling Correction System  
### NLP-Based Intelligent Text Correction Web Application

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)]
[![NLP](https://img.shields.io/badge/Domain-NLP-green)]
[![Status](https://img.shields.io/badge/Project-Production%20Ready-success)]

---

##  Project Summary

Developed an end-to-end NLP-powered web application that detects and corrects spelling mistakes, grammatical errors, and contextual inconsistencies in English text.

The system combines:

- Rule-based linguistic validation  
- Edit-distance spelling correction  
- Transformer-based contextual refinement  

Built with a modular architecture and deployed using Streamlit for real-time user interaction.

---

##  Business Problem

Poor grammar and spelling reduce communication clarity, professionalism, and credibility in academic, business, and digital environments.

This project addresses:

- Typographical errors  
- Subject–verb agreement issues  
- Tense inconsistencies  
- Article and preposition misuse  
- Contextual word misuse  

The solution improves readability and enhances written communication efficiency.

---

##  System Architecture


---
User Input (Streamlit UI)
↓
Text Preprocessing
↓
Spelling Correction Engine
↓
Rule-Based Grammar Checker
↓
ML-Based Contextual Correction (Transformers)
↓
Corrected Output Display


---

##  Technology Stack

### Frontend
- **Streamlit** – Interactive Web Application Framework  

### Backend
- **Python**

### NLP & ML Libraries
- **NLTK** – Tokenization, POS tagging  
- **spaCy** – Syntactic parsing  
- **TextBlob** – Basic correction support  
- **HuggingFace Transformers** – Contextual grammar correction  
- **Levenshtein Distance Algorithm** – Spelling similarity detection  

---

##  Processing Pipeline

###  Text Input
User enters text into the Streamlit application.

###  Text Preprocessing
- Lowercasing  
- Tokenization  
- POS tagging  
- Noise removal  

###  Spelling Correction
- Dictionary matching  
- Edit distance (Levenshtein)  

###  Grammar Correction

**Rule-based checks:**
- Subject–verb agreement  
- Tense consistency  
- Article usage  
- Preposition errors  

**Transformer-based contextual refinement**

###  Output Rendering
- Displays corrected text  
- Optional original vs corrected comparison  

---

##  Example

### Input
She go to market yesturday to buy vegetable.


### Output
She went to the market yesterday to buy vegetables.

### Improvements Applied
- Verb tense correction  
- Spelling correction  
- Plural agreement  
- Article insertion  

---

##  Project Structure

grammar-spell-correction/
│
├── app.py # Streamlit application
├── requirements.txt # Dependencies
├── utils/ # Helper functions
├── models/ # ML model integrations
└── README.md # Project documentation

---

##  Installation & Setup

###  Clone Repository

``
git clone https://github.com/your-username/grammar-spell-correction.git
cd grammar-spell-correction ``

Create Virtual Environment 
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows

Install Dependencies
pip install -r requirements.txt

Run Application
streamlit run app.py

The app runs at:
http://localhost:8501

## Use Cases

Academic writing assistance

Professional email proofreading

Content creation support

Non-native English language assistance

NLP learning demonstration project

## Future Enhancements

Multilingual grammar correction

GPT-based advanced contextual rewriting

Highlighted error explanations

Cloud deployment (Streamlit Cloud / AWS / Render)

Integration with document editors

## Academic Context

Course: Natural Language Processing
Program: M.Sc. Data Analytics (CBCS)
Institution: CHRIST (Deemed to be University), Bangalore
Author: Someshwar M

## License

This project is developed for academic and educational purposes.
Open for learning, enhancement, and portfolio demonstration.


