from app.agents.llm_architecture_search_agent import (
    LLMArchitectureSearchAgent
)

from app.agents.cloud_deployment_planner_agent import (
    CloudDeploymentPlannerAgent
)

from app.agents.memory_planner_agent import (
    MemoryPlannerAgent
)

from app.agents.workflow_executor_agent import (
    WorkflowExecutorAgent
)

from app.agents.debate_agent import (
    DebateAgent
)


class ControlTowerAgent:

    def execute(
        self,
        project_context
    ):

        architecture_agent = (
            LLMArchitectureSearchAgent()
        )

        architecture_plan = (
            architecture_agent.search(
                project_context
            )
        )

        deployment_agent = (
            CloudDeploymentPlannerAgent()
        )

        deployment_plan = (
            deployment_agent.plan(
                project_context
            )
        )

        planner = (
            MemoryPlannerAgent()
        )

        planning_decision = (
            planner.plan(
                project_context
            )
        )

        debate = (
            DebateAgent()
        )

        debate_result = (
            debate.debate(

                architect_view=
                    architecture_plan,

                optimization_view=
                    planning_decision,

                deployment_view=
                    deployment_plan
            )
        )

        workflow = (
            WorkflowExecutorAgent()
        )

        workflow_result = (
            workflow.execute(
                project_context
            )
        )

        return {

            "architecture_plan":
                architecture_plan,

            "deployment_plan":
                deployment_plan,

            "planning_decision":
                planning_decision,

            "debate_result":
                debate_result,

            "workflow_result":
                workflow_result
        }