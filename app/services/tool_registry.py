from app.agents.training_agent import (
    TrainingAgent
)

from app.agents.optimization_agent import (
    OptimizationAgent
)

from app.agents.deployment_strategy_agent import (
    DeploymentStrategyAgent
)


class ToolRegistry:

    def execute(
        self,
        action,
        context=None
    ):

        context = context or {}

        if action == "retrain_model":

            trainer = (
                TrainingAgent()
            )

            training_plan = {

                "selected_model":
                    context.get(
                        "model",
                        "ResNet18"
                    ),

                "epochs":
                    2,

                "batch_size":
                    32,

                "learning_rate":
                    0.001
            }

            result = (
                trainer.execute_training_plan(
                    training_plan
                )
            )

            return {

                "tool":
                    "TrainingAgent",

                "status":
                    "Completed",

                "result":
                    result[
                        "training_result"
                    ]
            }

        elif action == "optimize_model":

            optimizer = (
                OptimizationAgent()
            )

            result = (
                optimizer.optimize(
                    ["ResNet18"]
                )
            )

            return {

                "tool":
                    "OptimizationAgent",

                "status":
                    "Completed",

                "result":
                    result
            }

        elif action == "deploy_model":

            deployment = (
                DeploymentStrategyAgent()
            )

            result = (
                deployment.recommend(

                    context.get(
                        "intake_report",
                        {}
                    ),

                    context.get(
                        "model",
                        "ResNet18"
                    )
                )
            )

            return {

                "tool":
                    "DeploymentAgent",

                "status":
                    "Completed",

                "result":
                    result
            }

        return {

            "tool":
                None,

            "status":
                "No Action"
        }