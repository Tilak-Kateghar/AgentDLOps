from torchvision.datasets import CIFAR10


class CIFAR10Profiler:

    def profile(self):

        dataset = CIFAR10(
            root="./datasets",
            train=True,
            download=False
        )

        num_classes = len(
            dataset.classes
        )

        total_images = len(
            dataset
        )

        return {
            "dataset_name": "CIFAR10",
            "num_classes": num_classes,
            "total_images": total_images,
            "classes": dataset.classes
        }