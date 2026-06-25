class DecisionEngineAgent:

    def decide(
        self,
        optimization_result,
        deployment_result,
        cost_result
    ):

        return {

            "selected_model":
                optimization_result[
                    "best_architecture"
                ][
                    "model"
                ],

            "accuracy":
                optimization_result[
                    "best_hyperparameter"
                ][
                    "accuracy"
                ],

            "deployment":
                deployment_result[
                    "deployment_platform"
                ],

            "cost":
                cost_result[
                    "estimated_monthly_cost"
                ],

            "reasoning":
                (
                    "Best balance of "
                    "accuracy, deployment "
                    "readiness and cost"
                )
        }