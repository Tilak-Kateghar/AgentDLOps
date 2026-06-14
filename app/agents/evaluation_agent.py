class EvaluationAgent:
    """
    Evaluation Agent

    Produces a complete
    evaluation report.
    """

    def evaluate(
        self,
        training_result,
        metric_report
    ):

        accuracy = (
            metric_report["accuracy"]
        )

        if accuracy >= 80:

            status = "excellent"

        elif accuracy >= 50:

            status = "good"

        else:

            status = "needs_improvement"

        return {
            "average_loss":
                training_result[
                    "average_loss"
                ],

            "accuracy":
                metric_report[
                    "accuracy"
                ],

            "precision":
                metric_report[
                    "precision"
                ],

            "recall":
                metric_report[
                    "recall"
                ],

            "f1_score":
                metric_report[
                    "f1_score"
                ],

            "status":
                status
        }