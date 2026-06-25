from app.core.database import (
    SessionLocal
)

from app.models.project_run import (
    ProjectRun
)


class ProjectHistoryAgent:

    def save_run(
        self,
        intake_report,
        optimization_result
    ):

        db = SessionLocal()

        run = ProjectRun(

            project_type=
            intake_report[
                "problem_type"
            ],

            dataset_type=
            intake_report[
                "dataset_type"
            ],

            deployment_target=
            intake_report[
                "deployment_target"
            ],

            architecture=
            optimization_result[
                "best_architecture"
            ][
                "model"
            ],

            learning_rate=
            optimization_result[
                "best_hyperparameter"
            ][
                "learning_rate"
            ],

            accuracy=
            optimization_result[
                "best_hyperparameter"
            ][
                "accuracy"
            ]
        )

        db.add(run)

        db.commit()

        db.close()