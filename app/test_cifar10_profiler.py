from app.services.cifar10_profiler import (
    CIFAR10Profiler
)


def main():

    profiler = CIFAR10Profiler()

    report = profiler.profile()

    print("\nCIFAR10 PROFILE")
    print("=" * 40)

    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()