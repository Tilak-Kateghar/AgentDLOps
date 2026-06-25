class RollbackAgent:

    def evaluate(
        self,
        baseline_accuracy,
        current_accuracy,
        threshold=3.0
    ):

        drop = (
            baseline_accuracy
            - current_accuracy
        )

        rollback = (
            drop > threshold
        )

        return {

            "baseline":
                baseline_accuracy,

            "current":
                current_accuracy,

            "drop":
                round(
                    drop,
                    2
                ),

            "rollback":
                rollback
        }