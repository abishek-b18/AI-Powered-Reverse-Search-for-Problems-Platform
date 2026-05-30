from flask import Flask, render_template, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load Models
sentiment_model = joblib.load("models/sentiment_model.pkl")
opportunity_model = joblib.load("models/opportunity_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/problems")
def problems():
    try:
        data = pd.read_csv("datasets/complaints.csv")
        problems = data.to_dict(orient="records")
        return jsonify(problems)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/analyze")
def analyze():
    sample_text = ["I waste too much time scrolling social media"]

    sentiment = sentiment_model.predict(sample_text)[0]

    score = opportunity_model.predict([[85, 90, 80, 70]])[0]

    return jsonify({
        "problem": sample_text[0],
        "sentiment": sentiment,
        "opportunity_score": round(score, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)