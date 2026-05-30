import pandas as pd
from collections import Counter


class ProblemDetector:

    def __init__(self):
        pass

    def detect_common_problems(self, dataframe):

        categories = dataframe["category"]

        counts = Counter(categories)

        results = []

        for category, count in counts.items():

            results.append({
                "problem_category": category,
                "frequency": count
            })

        return sorted(
            results,
            key=lambda x: x["frequency"],
            reverse=True
        )


if __name__ == "__main__":

    df = pd.read_csv("datasets/complaints.csv")

    detector = ProblemDetector()

    print(detector.detect_common_problems(df))