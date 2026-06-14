from torchvision import datasets


def inspect_cifar10():

    train_dataset = datasets.CIFAR10(
        root="datasets",
        train=True,
        download=False
    )

    print("\nDATASET INFORMATION")
    print("=" * 40)

    print("Total Images:", len(train_dataset))

    print("Classes:")
    print(train_dataset.classes)

    image, label = train_dataset[0]

    print("\nFirst Image Size:")
    print(image.size)

    print("\nFirst Image Label:")
    print(label)

    print("\nFirst Image Class:")
    print(train_dataset.classes[label])


if __name__ == "__main__":
    inspect_cifar10()