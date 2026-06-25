from app.agents.memory_planner_agent import (
    MemoryPlannerAgent
)

from app.services.tool_registry import (
    ToolRegistry
)

import json


class WorkflowExecutorAgent:

    def execute(
        self,
        system_state
    ):

        planner = (
            MemoryPlannerAgent()
        )

        plan = (
            planner.plan(
                system_state
            )
        )

        try:

            decision = json.loads(

                plan.replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        except Exception:

            decision = {

                "action":
                    "monitor_only",

                "reason":
                    "Unable to parse plan"
            }

        registry = (
            ToolRegistry()
        )

        execution = (
            registry.execute(

                decision[
                    "action"
                ],

                context=
                system_state
            )
        )

        return {

            "decision":
                decision,

            "execution":
                execution
        }