import os
print("Files in folder:", os.listdir())
from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load dataset
df = pd.read_csv("news.csv")
df = df.dropna()

# Features and Labels
X = df['text']
y = df['label']

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X = vectorizer.fit_transform(X)

# Model Training
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Route
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""

    if request.method == 'POST':
        news = request.form.get('news')   # safe method

        if news:
            vect = vectorizer.transform([news])
            result = model.predict(vect)

            if result[0] == 'FAKE':
                prediction = "FAKE NEWS ❌"
            else:
                prediction = "REAL NEWS ✅"

    return render_template('index.html', prediction=prediction)

# Run App
if __name__ == "__main__":
    app.run(debug=True)