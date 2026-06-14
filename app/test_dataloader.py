from app.services.dataset_loader import DatasetLoader


def main():

    loader = DatasetLoader()

    train_loader, test_loader = (
        loader.load_cifar10(
            batch_size=64
        )
    )

    print("\nDATA LOADER REPORT")
    print("=" * 40)

    print(
        "Train Batches:",
        len(train_loader)
    )

    print(
        "Test Batches:",
        len(test_loader)
    )

    images, labels = next(
        iter(train_loader)
    )

    print(
        "\nBatch Shape:",
        images.shape
    )

    print(
        "Labels Shape:",
        labels.shape
    )


if __name__ == "__main__":
    main()