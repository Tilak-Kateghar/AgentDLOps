import torch

from app.models.model_factory import (
    ModelFactory
)

from app.services.dataset_loader import (
    DatasetLoader
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

    images, labels = next(
        iter(train_loader)
    )

    criterion = torch.nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )

    outputs = model(images)

    loss = criterion(
        outputs,
        labels
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print("\nTRAINING STEP REPORT")
    print("=" * 40)

    print("Loss:", loss.item())

    print(
        "Training step completed successfully."
    )


if __name__ == "__main__":
    main()