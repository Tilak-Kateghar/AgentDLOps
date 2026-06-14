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

    train_loader, _ = (
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

    report = (
        executor.train_one_epoch(
            model,
            train_loader,
            optimizer,
            criterion
        )
    )

    print("\nTRAIN ONE EPOCH REPORT")
    print("=" * 40)

    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()