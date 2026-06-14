from app.services.mlflow_tracker import (
    MLflowTracker
)


def main():

    tracker = MLflowTracker()

    tracker.start_run()

    tracker.log_param(
        "model",
        "EfficientNetB0"
    )

    tracker.log_param(
        "batch_size",
        32
    )

    tracker.log_metric(
        "accuracy",
        11.23
    )

    tracker.log_metric(
        "loss",
        2.40
    )

    tracker.end_run()

    print(
        "\nMLflow Test Completed"
    )


if __name__ == "__main__":
    main()