from app.agents.training_agent import (
    TrainingAgent
)

from app.services.dataset_loader import (
    DatasetLoader
)

from app.services.training_executor import (
    TrainingExecutor
)

from app.services.metric_evaluator import (
    MetricEvaluator
)


class ArchitectureBenchmarkAgent:

    def benchmark(
        self,
        candidate_models
    ):

        benchmark_results = []

        trainer = (
            TrainingAgent()
        )

        for model_name in candidate_models:

            plan = {

                "selected_model":
                    model_name,

                "epochs":
                    2,

                "batch_size":
                    32,

                "optimizer":
                    "Adam"
            }

            training_execution = (
                trainer.execute_training_plan(
                    plan
                )
            )

            model = (
                training_execution[
                    "trained_model"
                ]
            )

            test_loader = (
                training_execution[
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

            benchmark_results.append({

                "model":
                    model_name,

                "accuracy":
                    metrics[
                        "accuracy"
                    ]
            })

        return benchmark_results