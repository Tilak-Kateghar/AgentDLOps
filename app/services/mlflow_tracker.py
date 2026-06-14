import mlflow


class MLflowTracker:

    def __init__(self):

        mlflow.set_tracking_uri(
            "sqlite:///mlflow.db"
        )

        mlflow.set_experiment(
            "AgentDLOps"
        )

    def start_run(self):

        return mlflow.start_run()

    def log_param(
        self,
        key,
        value
    ):

        mlflow.log_param(
            key,
            value
        )

    def log_metric(
        self,
        key,
        value
    ):

        mlflow.log_metric(
            key,
            value
        )

    def log_artifact(
        self,
        file_path
    ):

        mlflow.log_artifact(
            file_path
        )

    def end_run(self):

        mlflow.end_run()