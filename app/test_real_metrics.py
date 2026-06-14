import torch

from app.models.model_factory import (
    ModelFactory
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


def main():

    model = ModelFactory.create_model(
        "MobileNetV3",
        num_classes=10
    )

    loader = DatasetLoader()

    train_loader, test_loader = (
        loader.load_cifar10(
            batch_size=64
        )
    )

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )

    criterion = (
        torch.nn.CrossEntropyLoss()
    )

    executor = TrainingExecutor()

    executor.train_one_epoch(
        model,
        train_loader,
        optimizer,
        criterion
    )

    prediction_report = (
        executor.collect_predictions(
            model,
            test_loader
        )
    )

    evaluator = MetricEvaluator()

    metric_report = (
        evaluator.evaluate(
            prediction_report["y_true"],
            prediction_report["y_pred"]
        )
    )

    print("\nREAL METRIC REPORT")
    print("=" * 40)

    for key, value in metric_report.items():
        print(
            f"{key}: {value:.2f}"
        )


if __name__ == "__main__":
    main()