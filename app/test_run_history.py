from app.services.run_history import (
    RunHistory
)


def main():

    history = RunHistory()

    sample_run = {
        "model": "EfficientNetB0",
        "accuracy": 9.76
    }

    history.save_run(
        sample_run
    )

    runs = (
        history.load_history()
    )

    print(
        "\nRUN HISTORY REPORT"
    )

    print("=" * 40)

    print(runs)


if __name__ == "__main__":
    main()