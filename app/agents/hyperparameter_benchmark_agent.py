from app.agents.training_agent import (
    TrainingAgent
)

from app.services.training_executor import (
    TrainingExecutor
)

from app.services.metric_evaluator import (
    MetricEvaluator
)


class HyperparameterBenchmarkAgent:

    def benchmark(
        self,
        model_name,
        trials
    ):

        results = []

        trainer = (
            TrainingAgent()
        )

        for trial in trials:

            training_plan = {

                "selected_model":
                    model_name,

                "epochs":
                    2,

                "batch_size":
                    trial["batch_size"],

                "learning_rate":
                    trial["learning_rate"],

                "optimizer":
                    "Adam"
            }

            execution = (
                trainer.execute_training_plan(
                    training_plan
                )
            )

            model = (
                execution[
                    "trained_model"
                ]
            )

            test_loader = (
                execution[
                    "test_loader"
                ]
            )

            executor = (
                TrainingExecutor()
            )

            prediction_report = (
                executor.collect_predictions(
                    model,
                    test_loader
                )
            )

            evaluator = (
                MetricEvaluator()
            )

            metrics = (
                evaluator.evaluate(
                    prediction_report[
                        "y_true"
                    ],
                    prediction_report[
                        "y_pred"
                    ]
                )
            )

            results.append({

                "learning_rate":
                    trial[
                        "learning_rate"
                    ],

                "batch_size":
                    trial[
                        "batch_size"
                    ],

                "accuracy":
                    metrics[
                        "accuracy"
                    ]
            })

        return results