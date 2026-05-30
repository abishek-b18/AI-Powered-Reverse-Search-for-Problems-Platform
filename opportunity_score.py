class OpportunityScorer:

    def calculate_score(
        self,
        frequency,
        severity,
        market_demand,
        competition
    ):

        score = (
            frequency * 0.30 +
            severity * 0.25 +
            market_demand * 0.30 +
            (100 - competition) * 0.15
        )

        return round(score, 2)

    def generate_report(
        self,
        problem_name,
        frequency,
        severity,
        market_demand,
        competition
    ):

        score = self.calculate_score(
            frequency,
            severity,
            market_demand,
            competition
        )

        return {
            "problem": problem_name,
            "opportunity_score": score,
            "frequency": frequency,
            "severity": severity,
            "market_demand": market_demand,
            "competition": competition
        }


if __name__ == "__main__":

    scorer = OpportunityScorer()

    result = scorer.generate_report(
        "Digital Addiction",
        90,
        85,
        95,
        40
    )

    print(result)