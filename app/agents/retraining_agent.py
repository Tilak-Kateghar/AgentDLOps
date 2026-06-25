from app.agents.drift_detection_agent import (
    DriftDetectionAgent
)

from app.services.optimization_pipeline import (
    OptimizationPipeline
)


class RetrainingAgent:

    def retrain_if_needed(
        self,
        intake_report,
        training_mean,
        live_mean
    ):

        drift_agent = (
            DriftDetectionAgent()
        )

        drift_report = (
            drift_agent.detect(
                training_mean,
                live_mean
            )
        )

        if not drift_report[
            "drift_detected"
        ]:

            return {

                "retraining_triggered":
                    False,

                "drift_report":
                    drift_report
            }

        optimizer = (
            OptimizationPipeline()
        )

        optimization_result = (
            optimizer.execute(
                intake_report
            )
        )

        return {

            "retraining_triggered":
                True,

            "drift_report":
                drift_report,

            "optimization_result":
                optimization_result
        }