import joblib

class SentimentAnalyzer:

    def __init__(self):
        self.model = joblib.load("models/sentiment_model.pkl")

    def predict_sentiment(self, text):

        result = self.model.predict([text])[0]

        return {
            "text": text,
            "sentiment": result
        }


if __name__ == "__main__":

    analyzer = SentimentAnalyzer()

    sample = "I waste too much time scrolling social media"

    print(analyzer.predict_sentiment(sample))