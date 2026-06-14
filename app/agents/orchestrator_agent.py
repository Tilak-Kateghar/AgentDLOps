from app.agents.dataset_agent import (
    DatasetAgent
)

from app.agents.architecture_agent import (
    ArchitectureAgent
)

from app.agents.training_agent import (
    TrainingAgent
)

from app.agents.evaluation_agent import (
    EvaluationAgent
)

from app.services.dataset_loader import (
    DatasetLoader
)

from app.services.training_executor import (
    TrainingExecutor
)

from app.models.model_factory import (
    ModelFactory
)

from app.services.metric_evaluator import (
    MetricEvaluator
)

from app.services.run_history import (
    RunHistory
)

from app.services.performance_comparator import (
    PerformanceComparator
)

from app.services.adaptive_strategy import (
    AdaptiveStrategy
)

from app.services.architecture_reviewer import (
    ArchitectureReviewer
)

class OrchestratorAgent:

    def run_pipeline(self):

        dataset_agent = DatasetAgent(
            dataset_path="datasets/test_dataset"
        )

        dataset_report = (
            dataset_agent.analyze()
        )

        architecture_agent = (
            ArchitectureAgent()
        )

        recommendation = (
            architecture_agent.recommend(
                dataset_report
            )
        )

        training_agent = (
            TrainingAgent()
        )

        training_execution = (
            training_agent.execute_training(
                dataset_report,
                recommendation
            )
        )

        training_plan = (
            training_execution[
                "training_plan"
            ]
        )

        training_result = (
            training_execution[
                "training_result"
            ]
        )

        model_path = (
            training_execution[
                "model_path"
            ]
        )

        loader = DatasetLoader()

        _, test_loader = (
            loader.load_cifar10(
                batch_size=64
            )
        )

        model = ModelFactory.create_model(
            training_plan[
                "selected_model"
            ],
            num_classes=10
        )

        executor = TrainingExecutor()

        prediction_report = (
            executor.collect_predictions(
                model,
                test_loader
            )
        )

        evaluator = MetricEvaluator()

        metric_report = (
            evaluator.evaluate(
                prediction_report[
                    "y_true"
                ],
                prediction_report[
                    "y_pred"
                ]
            )
        )

        evaluation_agent = (
            EvaluationAgent()
        )

        evaluation_report = (
            evaluation_agent.evaluate(
                training_result,
                metric_report
            )
        )

        history_manager = (
            RunHistory()
        )

        current_run = {

            "model":
                training_plan[
                    "selected_model"
                ],

            "accuracy":
                evaluation_report[
                    "accuracy"
                ]
        }

        history_manager.save_run(
            current_run
        )

        history = (
            history_manager.load_history()
        )

        comparator = (
            PerformanceComparator()
        )

        comparison_report = (
            comparator.compare(
                history
            )
        )

        reviewer = (
            ArchitectureReviewer()
        )

        architecture_review = (
            reviewer.review(
                recommendation,
                comparison_report
            )
        )

        strategy = (
            AdaptiveStrategy()
        )

        adaptive_plan = (
            strategy.adapt(
                training_plan,
                comparison_report
            )
        )

        return {
            "architecture_review":
                architecture_review,

            "comparison_report":
                comparison_report,

            "adaptive_plan":
                adaptive_plan,

            "dataset_report":
                dataset_report,

            "recommendation":
                recommendation,

            "training_plan":
                training_plan,

            "training_result":
                training_result,

            "evaluation_report":
                evaluation_report,

            "model_path":
                model_path,
        }