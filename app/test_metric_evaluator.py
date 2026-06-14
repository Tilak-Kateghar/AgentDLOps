from app.services.metric_evaluator import (
    MetricEvaluator
)


def main():

    y_true = [
        0, 1, 2, 0, 1,
        2, 0, 1, 2, 0
    ]

    y_pred = [
        0, 1, 2, 0, 0,
        2, 0, 1, 1, 0
    ]

    evaluator = MetricEvaluator()

    report = evaluator.evaluate(
        y_true,
        y_pred
    )

    print("\nMETRIC REPORT")
    print("=" * 40)

    for key, value in report.items():
        print(
            f"{key}: {value:.2f}"
        )


if __name__ == "__main__":
    main()