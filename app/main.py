from app.agents.orchestrator_agent import (
    OrchestratorAgent
)


def main():

    orchestrator = (
        OrchestratorAgent()
    )

    result = (
        orchestrator.run_pipeline()
    )

    print("\nDATASET REPORT")
    print("=" * 40)

    for key, value in result[
        "dataset_report"
    ].items():

        print(
            f"{key}: {value}"
        )

    print(
        "\nMODEL RECOMMENDATIONS"
    )

    print("=" * 40)

    recommendation = result[
        "recommendation"
    ]

    print("Scores:")

    for model, score in (
        recommendation[
            "scores"
        ].items()
    ):

        print(
            f"{model}: {score}"
        )

    print(
        "\nRanked Recommendations:"
    )

    print(
        recommendation[
            "recommended_models"
        ]
    )

    print("\nDECISION REASON")
    print("=" * 40)

    for key, value in (
        recommendation[
            "decision_reason"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )

    print("\nTRAINING PLAN")
    print("=" * 40)

    for key, value in (
        result[
            "training_plan"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )

    print("\nTRAINING RESULT")
    print("=" * 40)

    for key, value in (
        result[
            "training_result"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )

    print("\nMODEL REGISTRY")
    print("=" * 40)

    print(
        f"saved_model: "
        f"{result['model_path']}"
    )

    print("\nEVALUATION REPORT")
    print("=" * 40)

    for key, value in (
        result[
            "evaluation_report"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()