class DriftDetectionAgent:

    def detect(
        self,
        training_mean,
        live_mean,
        threshold=0.10
    ):

        drift_score = abs(
            training_mean -
            live_mean
        )

        drift_detected = (
            drift_score >
            threshold
        )

        return {

            "training_mean":
                training_mean,

            "live_mean":
                live_mean,

            "drift_score":
                round(
                    drift_score,
                    4
                ),

            "threshold":
                threshold,

            "drift_detected":
                drift_detected
        }