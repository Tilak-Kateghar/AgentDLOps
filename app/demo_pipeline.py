from app.services.uploaded_dataset_inspector import (
    UploadedDatasetInspector
)

from app.agents.project_intake_agent import (
    ProjectIntakeAgent
)

from app.agents.candidate_family_agent import (
    CandidateFamilyAgent
)

from app.services.optimization_pipeline import (
    OptimizationPipeline
)

from app.agents.deployment_strategy_agent import (
    DeploymentStrategyAgent
)

from app.agents.control_tower_agent import (
    ControlTowerAgent
)

from app.agents.research_paper_agent import (
    ResearchPaperAgent
)


class DemoPipeline:

    def run(
        self,
        dataset_path,
        project_context
    ):

        # STEP 1
        inspector = UploadedDatasetInspector()

        dataset_report = (
            inspector.inspect(
                dataset_path
            )
        )

        # STEP 2
        intake_agent = (
            ProjectIntakeAgent()
        )

        intake_report = (
            intake_agent.collect_requirements(

                project_context["problem_type"],
                project_context["problem_statement"],
                project_context["expected_outcome"],
                project_context["dataset_type"],
                project_context["deployment_target"],
                project_context["optimization_priority"]
            )
        )

        # STEP 3
        candidate_agent = (
            CandidateFamilyAgent()
        )

        candidate_result = (
            candidate_agent.recommend(
                intake_report
            )
        )

        # STEP 4
        optimizer = (
            OptimizationPipeline()
        )

        optimization_result = (
            optimizer.execute(
                intake_report
            )
        )

        # STEP 5
        best_model = (
            optimization_result[
                "best_architecture"
            ]["model"]
        )

        deployment_agent = (
            DeploymentStrategyAgent()
        )

        deployment_result = (
            deployment_agent.recommend(
                intake_report,
                best_model
            )
        )

        # STEP 6
        control_tower = (
            ControlTowerAgent()
        )

        control_result = (
            control_tower.execute(
                intake_report
            )
        )

        # STEP 7
        paper_agent = (
            ResearchPaperAgent()
        )

        paper = (
            paper_agent.generate(
                {
                    "dataset_report":
                        dataset_report,

                    "optimization_result":
                        optimization_result,

                    "deployment":
                        deployment_result
                }
            )
        )

        return {

            "dataset_report":
                dataset_report,

            "candidate_result":
                candidate_result,

            "optimization_result":
                optimization_result,

            "deployment_result":
                deployment_result,

            "control_result":
                control_result,

            "research_paper":
                paper
        }