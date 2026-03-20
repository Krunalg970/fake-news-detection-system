# 📰 Fake News Detection System

This project is a **Machine Learning-based web application** that detects whether a news article is **Fake or Real** using Natural Language Processing (NLP).

## 🚀 Features
- Detect Fake & Real News
- Simple Web Interface (Flask)
- Fast Prediction using ML Model
- Easy to Use

## 🧠 Technologies Used
- Python
- Flask (Web Framework)
- Pandas
- Scikit-learn
- NLP (TF-IDF)
- Logistic Regression

## ⚙️ How It Works
1. User enters news text
2. Text is preprocessed (cleaning)
3. TF-IDF converts text into numbers
4. Logistic Regression model predicts result
5. Output shown as **FAKE ❌ or REAL ✅**

## 📁 Project Structure
fake_news_detector/
│
├── app.py
├── news.csv
├── requirements.txt
└── templates/
└── index.html

## ▶️ How to Run Project

### 1. Install dependencies
pip install flask pandas scikit-learn

### 2. Run the app
python app.py

### 3. Open in browser
http://127.0.0.1:5000

## 📊 Model Used
- Logistic Regression
- TF-IDF Vectorizer
  
## 🎯 Output
- REAL NEWS ✅
- FAKE NEWS ❌

## 📌 Future Improvements
- Use Deep Learning (LSTM, BERT)
- Add real-time news API
- Improve accuracy

## 👨‍💻 Author
**Krunal Goswami**
