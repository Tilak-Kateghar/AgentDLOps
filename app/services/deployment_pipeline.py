from app.agents.autonomous_deployment_agent import (
    AutonomousDeploymentAgent
)

from app.agents.cost_estimation_agent import (
    CostEstimationAgent
)


class DeploymentPipeline:

    def execute(
        self,
        intake_report,
        optimization_result
    ):

        deployment_agent = (
            AutonomousDeploymentAgent()
        )

        deployment_result = (
            deployment_agent.recommend(
                intake_report,
                optimization_result
            )
        )

        cost_agent = (
            CostEstimationAgent()
        )

        cost_result = (
            cost_agent.estimate(
                deployment_result
            )
        )

        return {

            "deployment":
                deployment_result,

            "cost":
                cost_result
        }