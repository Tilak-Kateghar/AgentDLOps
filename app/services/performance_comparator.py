class PerformanceComparator:

    def compare(
        self,
        history
    ):

        if len(history) < 2:

            return {
                "status":
                "not_enough_history"
            }

        previous = history[-2]

        current = history[-1]

        previous_acc = (
            previous["accuracy"]
        )

        current_acc = (
            current["accuracy"]
        )

        if current_acc > previous_acc:

            status = "improved"

        elif current_acc < previous_acc:

            status = "degraded"

        else:

            status = "unchanged"

        return {

            "previous_accuracy":
                previous_acc,

            "current_accuracy":
                current_acc,

            "status":
                status
        }