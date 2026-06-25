class DecisionEngine:

    def generate_decision(
        self,
        intake_report,
        architecture_result,
        hyperparameter_result,
        deployment_result,
        champion_model
    ):

        return {

            "problem_type":
                intake_report[
                    "problem_type"
                ],

            "dataset_type":
                intake_report[
                    "dataset_type"
                ],

            "deployment_target":
                intake_report[
                    "deployment_target"
                ],

            "selected_architecture":
                architecture_result[
                    "model"
                ],

            "architecture_accuracy":
                architecture_result[
                    "accuracy"
                ],

            "learning_rate":
                hyperparameter_result[
                    "learning_rate"
                ],

            "hyperparameter_accuracy":
                hyperparameter_result[
                    "accuracy"
                ],

            "deployment_platform":
                deployment_result[
                    "platform"
                ],

            "deployment_format":
                deployment_result[
                    "format"
                ],

            "champion_model":
                champion_model
        }