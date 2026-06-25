from app.services.uploaded_dataset_inspector import (
    UploadedDatasetInspector
)

from app.agents.project_intake_agent import (
    ProjectIntakeAgent
)

from app.services.optimization_pipeline import (
    OptimizationPipeline
)

from app.agents.control_tower_agent import (
    ControlTowerAgent
)

from app.agents.research_paper_agent import (
    ResearchPaperAgent
)

from app.agents.self_improving_agent import (
    SelfImprovingAgent
)


class AutonomousPipeline:

    def run(
        self,
        dataset_path,
        project_context
    ):

        print("\n[1/6] DATASET ANALYSIS")

        inspector = (
            UploadedDatasetInspector()
        )

        dataset_report = (
            inspector.inspect(
                dataset_path
            )
        )

        print(dataset_report)

        print("\n[2/6] PROJECT INTAKE")

        intake_agent = (
            ProjectIntakeAgent()
        )

        intake_report = (
            intake_agent.collect_requirements(

                project_context[
                    "problem_type"
                ],

                project_context[
                    "problem_statement"
                ],

                project_context[
                    "expected_outcome"
                ],

                project_context[
                    "dataset_type"
                ],

                project_context[
                    "deployment_target"
                ],

                project_context[
                    "optimization_priority"
                ]
            )
        )

        print(intake_report)

        print("\n[3/6] OPTIMIZATION PIPELINE")

        optimizer = (
            OptimizationPipeline()
        )

        optimization_result = (
            optimizer.execute(
                intake_report
            )
        )

        print(
            optimization_result[
                "best_architecture"
            ]
        )

        print("\n[4/6] CONTROL TOWER")

        control_tower = (
            ControlTowerAgent()
        )

        control_result = (
            control_tower.execute(

                {
                    **intake_report,

                    "accuracy":
                    optimization_result[
                        "best_architecture"
                    ].get(
                        "accuracy",
                        0
                    )
                }
            )
        )

        print(
            control_result[
                "workflow_result"
            ]
        )

        print("\n[5/6] SELF IMPROVEMENT")

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

        print(
            learning_result
        )

        print("\n[6/6] RESEARCH REPORT")

        paper_agent = (
            ResearchPaperAgent()
        )

        paper = (
            paper_agent.generate(

                {
                    "dataset":
                    dataset_report,

                    "optimization":
                    optimization_result,

                    "control":
                    control_result
                }
            )
        )

        return {

            "dataset_report":
                dataset_report,

            "intake_report":
                intake_report,

            "optimization_result":
                optimization_result,

            "control_result":
                control_result,

            "learning_result":
                learning_result,

            "research_paper":
                paper
        }