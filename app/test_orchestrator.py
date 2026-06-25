# from app.agents.orchestrator_agent import (
#     OrchestratorAgent
# )


# def main():

#     orchestrator = (
#         OrchestratorAgent()
#     )

#     result = (
#         orchestrator.run_pipeline()
#     )

#     print(
#         "\nORCHESTRATOR REPORT"
#     )

#     print("=" * 40)

#     print(
#         result["training_plan"]
#     )

#     print(
#         result["evaluation_report"]
#     )


# if __name__ == "__main__":
#     main()

from app.agents.orchestrator_agent import (
    OrchestratorAgent
)

agent = (
    OrchestratorAgent()
)

result = (
    agent.run({

        "problem_type":
            "image_classification",

        "dataset_type":
            "image",

        "deployment_target":
            "mobile",

        "optimization_priority":
            "latency"
    })
)

print()
print(
    "FINAL ORCHESTRATION REPORT"
)
print("=" * 40)

print(
    result["optimization"]
)

print()

print(
    result["explanation"]
)