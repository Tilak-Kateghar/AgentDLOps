from torchvision import datasets


def test_resolution():

    dataset = datasets.CIFAR10(
        root="datasets",
        train=True,
        download=False
    )

    total_width = 0
    total_height = 0

    sample_size = 100

    for i in range(sample_size):

        image, label = dataset[i]

        width, height = image.size

        total_width += width
        total_height += height

    avg_width = total_width / sample_size
    avg_height = total_height / sample_size

    print("\nRESOLUTION REPORT")
    print("=" * 40)

    print("Average Width :", avg_width)
    print("Average Height:", avg_height)


if __name__ == "__main__":
    test_resolution()