from app.services.architecture_reviewer import (
    ArchitectureReviewer
)


def main():

    recommendation = {

        "recommended_models": [

            "EfficientNetB0",

            "ResNet50",

            "MobileNetV3"
        ]
    }

    comparison_report = {

        "status":
            "degraded"
    }

    reviewer = (
        ArchitectureReviewer()
    )

    result = reviewer.review(
        recommendation,
        comparison_report
    )

    print(
        "\nARCHITECTURE REVIEW REPORT"
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