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
        "MobileNetV3"
    )

    loader = DatasetLoader()

    train_loader, _ = (
        loader.load_cifar10(
            batch_size=64
        )
    )

    executor = TrainingExecutor()

    report = executor.forward_pass(
        model,
        train_loader
    )

    print("\nFORWARD PASS REPORT")
    print("=" * 40)

    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()