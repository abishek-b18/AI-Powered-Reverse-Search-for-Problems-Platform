class RecommendationEngine:

    def generate_recommendation(
        self,
        problem,
        score
    ):

        if score >= 85:

            level = "High Opportunity"

            suggestion = (
                f"Build a startup around '{problem}'. "
                f"Strong market demand detected."
            )

        elif score >= 70:

            level = "Medium Opportunity"

            suggestion = (
                f"Research and validate '{problem}' "
                f"before product development."
            )

        else:

            level = "Low Opportunity"

            suggestion = (
                f"Monitor '{problem}' and collect "
                f"additional market data."
            )

        return {
            "problem": problem,
            "score": score,
            "opportunity_level": level,
            "recommendation": suggestion
        }


if __name__ == "__main__":

    engine = RecommendationEngine()

    result = engine.generate_recommendation(
        "Digital Addiction",
        92
    )

    print(result)