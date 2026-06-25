import mlflow

from app.core.database import (
    SessionLocal
)

from app.models.project_run import (
    ProjectRun
)


class ExperimentTrackingAgent:

    def track(

        self,

        intake_report,

        optimization_result
    ):

        mlflow.set_experiment(
            "AgentDLOps"
        )

        with mlflow.start_run() as run:

            mlflow.log_param(

                "problem_type",

                intake_report[
                    "problem_type"
                ]
            )

            mlflow.log_param(

                "architecture",

                optimization_result[
                    "best_architecture"
                ][
                    "model"
                ]
            )

            mlflow.log_param(

                "learning_rate",

                optimization_result[
                    "best_hyperparameter"
                ][
                    "learning_rate"
                ]
            )

            mlflow.log_metric(

                "accuracy",

                optimization_result[
                    "best_hyperparameter"
                ][
                    "accuracy"
                ]
            )

            run_id = (
                run.info.run_id
            )

        db = SessionLocal()

        project_run = ProjectRun(

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

        db.add(
            project_run
        )

        db.commit()

        db.close()

        return {

            "mlflow_run_id":
                run_id
        }