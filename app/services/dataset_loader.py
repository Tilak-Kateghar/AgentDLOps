from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader


class DatasetLoader:

    def load_cifar10(
        self,
        batch_size=32
    ):

        transform = transforms.Compose([
            transforms.ToTensor()
        ])

        train_dataset = datasets.CIFAR10(
            root="datasets",
            train=True,
            download=False,
            transform=transform
        )

        test_dataset = datasets.CIFAR10(
            root="datasets",
            train=False,
            download=False,
            transform=transform
        )

        train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=True
        )

        test_loader = DataLoader(
            test_dataset,
            batch_size=batch_size,
            shuffle=False
        )

        return (
            train_loader,
            test_loader
        )