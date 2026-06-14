from app.services.adaptive_strategy import (
    AdaptiveStrategy
)


def main():

    training_plan = {

        "selected_model":
            "EfficientNetB0",

        "epochs":
            20,

        "batch_size":
            32
    }

    comparison_report = {

        "status":
            "degraded"
    }

    strategy = (
        AdaptiveStrategy()
    )

    result = strategy.adapt(
        training_plan,
        comparison_report
    )

    print(
        "\nADAPTIVE STRATEGY REPORT"
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