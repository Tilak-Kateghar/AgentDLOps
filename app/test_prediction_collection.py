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

    report = (
        executor.collect_predictions(
            model,
            test_loader
        )
    )

    print("\nPREDICTION REPORT")
    print("=" * 40)

    print(
        "True Labels:",
        len(report["y_true"])
    )

    print(
        "Predicted Labels:",
        len(report["y_pred"])
    )

    print(
        "\nFirst 10 Predictions:"
    )

    print(
        report["y_pred"][:10]
    )


if __name__ == "__main__":
    main()