from torchvision import datasets


def download_cifar10():

    datasets.CIFAR10(
        root="datasets",
        train=True,
        download=True
    )

    datasets.CIFAR10(
        root="datasets",
        train=False,
        download=True
    )

    print("CIFAR-10 downloaded successfully.")


if __name__ == "__main__":
    download_cifar10()