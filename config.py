import os

class Config:

    SECRET_KEY = "reverse_search_problem_secret_key"

    DATASET_PATH = "datasets/complaints.csv"

    SENTIMENT_MODEL = "models/sentiment_model.pkl"

    OPPORTUNITY_MODEL = "models/opportunity_model.pkl"

    MONGO_URI = "mongodb://localhost:27017/problem_discovery"

    DEBUG = True