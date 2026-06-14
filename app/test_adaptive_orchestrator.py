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
        "\nADAPTIVE REPORT"
    )

    print("=" * 40)

    for key, value in (
        result[
            "comparison_report"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )


if __name__ == "__main__":
    main()