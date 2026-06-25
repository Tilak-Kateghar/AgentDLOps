from app.agents.control_tower_agent import (
    ControlTowerAgent
)

from app.agents.self_improving_agent import (
    SelfImprovingAgent
)

from app.agents.research_paper_agent import (
    ResearchPaperAgent
)


class AgentDLOps:

    def run(
        self,
        project_context
    ):

        control_tower = (
            ControlTowerAgent()
        )

        control_result = (
            control_tower.execute(
                project_context
            )
        )

        learning_agent = (
            SelfImprovingAgent()
        )

        learning_result = (
            learning_agent.learn(

                decision=
                control_result[
                    "workflow_result"
                ][
                    "decision"
                ],

                outcome={
                    "status":
                        "completed"
                }
            )
        )

        paper_agent = (
            ResearchPaperAgent()
        )

        paper = (
            paper_agent.generate(
                project_context
            )
        )

        return {

            "control_tower":
                control_result,

            "learning":
                learning_result,

            "research_paper":
                paper
        }