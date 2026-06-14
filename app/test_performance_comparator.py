from app.services.performance_comparator import (
    PerformanceComparator
)


def main():

    history = [

        {
            "model":
            "EfficientNetB0",

            "accuracy":
            9.76
        },

        {
            "model":
            "EfficientNetB0",

            "accuracy":
            11.20
        }
    ]

    comparator = (
        PerformanceComparator()
    )

    result = (
        comparator.compare(
            history
        )
    )

    print(
        "\nCOMPARISON REPORT"
    )

    print("=" * 40)

    for key, value in (
        result.items()
    ):

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()