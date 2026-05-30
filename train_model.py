import pandas as pd
import numpy as np
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

# -----------------------------
# Sentiment Training Dataset
# -----------------------------

sentiment_data = pd.DataFrame({
    "text": [
        "I hate wasting time",
        "This product is terrible",
        "Students need better guidance",
        "Amazing application",
        "Excellent service",
        "Very useful platform"
    ],
    "label": [
        "Negative",
        "Negative",
        "Negative",
        "Positive",
        "Positive",
        "Positive"
    ]
})

# -----------------------------
# Sentiment Model
# -----------------------------

sentiment_model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

sentiment_model.fit(
    sentiment_data["text"],
    sentiment_data["label"]
)

joblib.dump(
    sentiment_model,
    "models/sentiment_model.pkl"
)

print("Sentiment Model Saved")

# -----------------------------
# Opportunity Score Dataset
# -----------------------------

X = np.array([
    [80, 90, 85, 70],
    [60, 75, 65, 50],
    [95, 92, 90, 85],
    [70, 65, 72, 60],
    [88, 85, 90, 80]
])

y = np.array([
    89,
    65,
    95,
    70,
    90
])

# Features:
# Frequency
# Severity
# Market Demand
# Competition

opportunity_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

opportunity_model.fit(X, y)

joblib.dump(
    opportunity_model,
    "models/opportunity_model.pkl"
)

print("Opportunity Model Saved")