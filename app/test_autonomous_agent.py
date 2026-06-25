from app.agents.autonomous_deployment_agent import (
    AutonomousDeploymentAgent
)

agent = (
    AutonomousDeploymentAgent()
)

result = (
    agent.recommend(

        {
            "deployment_target":
                "mobile"
        },

        {
            "best_architecture":
                {
                    "model":
                        "ResNet18"
                }
        }
    )
)

print()
print(
    "AUTONOMOUS DEPLOYMENT REPORT"
)
print("=" * 40)
print(result)