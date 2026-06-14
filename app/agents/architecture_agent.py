from app.services.architecture_rules import (
    ArchitectureScorer
)


class ArchitectureAgent:

    def recommend(self, dataset_report):

        scorer = ArchitectureScorer()

        scores = scorer.score(
            dataset_report
        )

        ranked_models = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = [
            model
            for model, score in ranked_models
        ]

        winner = recommendations[0]

        decision_reason = {
            "dataset_size": dataset_report[
                "dataset_size"
            ],
            "num_classes": dataset_report[
                "num_classes"
            ],
            "winner": winner,
            "winner_score": scores[winner]
        }

        return {
            "scores": scores,
            "recommended_models":
                recommendations,
            "decision_reason":
                decision_reason
        }