# app/services/intake_pipeline.py

from app.agents.project_intake_agent import (
    ProjectIntakeAgent
)

from app.agents.candidate_family_agent import (
    CandidateFamilyAgent
)

from app.agents.deployment_strategy_agent import (
    DeploymentStrategyAgent
)

from app.services.decision_engine import (
    DecisionEngine
)


class IntakePipeline:

    def execute(
        self,
        problem_type,
        problem_statement,
        expected_outcome,
        dataset_type,
        deployment_target,
        optimization_priority
    ):

        intake_agent = (
            ProjectIntakeAgent()
        )

        intake_report = (
            intake_agent.collect_requirements(
                problem_type,
                problem_statement,
                expected_outcome,
                dataset_type,
                deployment_target,
                optimization_priority
            )
        )

        candidate_agent = (
            CandidateFamilyAgent()
        )

        candidate_result = (
            candidate_agent.recommend(
                intake_report
            )
        )

        selected_model = (
            candidate_result[
                "candidates"
            ][0]
        )

        deployment_agent = (
            DeploymentStrategyAgent()
        )

        deployment_result = (
            deployment_agent.recommend(
                intake_report,
                selected_model
            )
        )

        decision_engine = (
            DecisionEngine()
        )

        decision = (
            decision_engine.generate_decision(
                intake_report,

                {
                    "model":
                        selected_model,

                    "accuracy":
                        0
                },

                {
                    "learning_rate":
                        0.001,

                    "accuracy":
                        0
                },

                deployment_result,

                selected_model
            )
        )

        return {

            "intake_report":
                intake_report,

            "candidate_result":
                candidate_result,

            "deployment_result":
                deployment_result,

            "decision":
                decision
        }