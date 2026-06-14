from app.agents.dataset_agent import DatasetAgent
from app.agents.architecture_agent import ArchitectureAgent
from app.agents.training_agent import TrainingAgent
from app.agents.evaluation_agent import EvaluationAgent
from app.services.training_executor import (
    TrainingExecutor
)
from app.services.mlflow_tracker import (
    MLflowTracker
)
from app.services.metric_evaluator import (
    MetricEvaluator
)


def main():

    # =====================================
    # DATASET AGENT
    # =====================================

    dataset_agent = DatasetAgent(
        dataset_path="datasets"
    )

    dataset_report = dataset_agent.analyze()

    # =====================================
    # ARCHITECTURE AGENT
    # =====================================

    architecture_agent = ArchitectureAgent()

    recommendation = (
        architecture_agent.recommend(
            dataset_report
        )
    )

    # =====================================
    # TRAINING AGENT
    # =====================================

    training_agent = TrainingAgent()

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

    trained_model = (
        training_execution[
            "trained_model"
        ]
    )

    test_loader = (
        training_execution[
            "test_loader"
        ]
    )

    # =====================================
    # METRIC EVALUATION
    # =====================================

    executor = TrainingExecutor()

    prediction_report = (
        executor.collect_predictions(
            trained_model,
            test_loader
        )
    )

    metric_evaluator = (
        MetricEvaluator()
    )

    metric_report = (
        metric_evaluator.evaluate(
            prediction_report["y_true"],
            prediction_report["y_pred"]
        )
    )

    # =====================================
    # EVALUATION AGENT
    # =====================================

    evaluation_agent = (
        EvaluationAgent()
    )

    evaluation_report = (
        evaluation_agent.evaluate(
            training_result,
            metric_report
        )
    )

    # =====================================
    # MLFLOW TRACKING
    # =====================================

    tracker = MLflowTracker()

    tracker.start_run()

    # Parameters

    tracker.log_param(
        "dataset",
        dataset_report["dataset_name"]
    )

    tracker.log_param(
        "selected_model",
        training_plan["selected_model"]
    )

    tracker.log_param(
        "batch_size",
        training_plan["batch_size"]
    )

    tracker.log_param(
        "epochs",
        training_plan["epochs"]
    )

    tracker.log_param(
        "dataset_size",
        recommendation[
            "decision_reason"
        ]["dataset_size"]
    )

    tracker.log_param(
        "num_classes",
        recommendation[
            "decision_reason"
        ]["num_classes"]
    )

    tracker.log_param(
        "winner_score",
        recommendation[
            "decision_reason"
        ]["winner_score"]
    )

    # Metrics

    tracker.log_metric(
        "MobileNetV3_score",
        recommendation[
            "scores"
        ]["MobileNetV3"]
    )

    tracker.log_metric(
        "EfficientNetB0_score",
        recommendation[
            "scores"
        ]["EfficientNetB0"]
    )

    tracker.log_metric(
        "ResNet50_score",
        recommendation[
            "scores"
        ]["ResNet50"]
    )

    tracker.log_metric(
        "loss",
        evaluation_report["average_loss"]
    )

    tracker.log_metric(
        "accuracy",
        evaluation_report["accuracy"]
    )

    tracker.log_metric(
        "precision",
        evaluation_report["precision"]
    )

    tracker.log_metric(
        "recall",
        evaluation_report["recall"]
    )

    tracker.log_metric(
        "f1_score",
        evaluation_report["f1_score"]
    )

    tracker.log_artifact(
        model_path
    )

    tracker.end_run()

    # =====================================
    # REPORTING
    # =====================================

    print("\nDATASET REPORT")
    print("=" * 40)

    for key, value in dataset_report.items():
        print(f"{key}: {value}")

    print("\nMODEL RECOMMENDATIONS")
    print("=" * 40)

    print("Scores:")

    for model, score in recommendation[
        "scores"
    ].items():

        print(
            f"{model}: {score}"
        )

    print(
        "\nRanked Recommendations:"
    )

    print(
        recommendation[
            "recommended_models"
        ]
    )

    print("\nDECISION REASON")
    print("=" * 40)

    for key, value in recommendation[
        "decision_reason"
    ].items():

        print(
            f"{key}: {value}"
        )

    print("\nTRAINING PLAN")
    print("=" * 40)

    for key, value in training_plan.items():
        print(f"{key}: {value}")

    print("\nTRAINING RESULT")
    print("=" * 40)

    for key, value in training_result.items():
        print(f"{key}: {value}")

    print("\nMODEL REGISTRY")
    print("=" * 40)
    print(f"saved_model: {model_path}")

    print("\nEVALUATION REPORT")
    print("=" * 40)

    for key, value in evaluation_report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()