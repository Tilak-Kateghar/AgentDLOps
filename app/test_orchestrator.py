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
        "\nORCHESTRATOR REPORT"
    )

    print("=" * 40)

    print(
        result["training_plan"]
    )

    print(
        result["evaluation_report"]
    )


if __name__ == "__main__":
    main()