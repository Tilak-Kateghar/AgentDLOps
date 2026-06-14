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

    print(
        "\nAUTONOMOUS ADAPTATION REPORT"
    )

    print("=" * 40)

    for key, value in (
        result[
            "adaptive_plan"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()