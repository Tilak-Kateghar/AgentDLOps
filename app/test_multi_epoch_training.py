from app.agents.training_agent import (
    TrainingAgent
)


def main():

    dataset_report = {

        "dataset_name":
            "CIFAR10",

        "num_classes":
            10,

        "dataset_size":
            "medium"
    }

    recommendation = {

        "recommended_models": [
            "EfficientNetB0"
        ]
    }

    agent = TrainingAgent()

    result = agent.execute_training(
        dataset_report,
        recommendation
    )

    print(
        "\nMULTI EPOCH REPORT"
    )

    print("=" * 40)

    for epoch in result[
        "epoch_history"
    ]:

        print(epoch)


if __name__ == "__main__":
    main()