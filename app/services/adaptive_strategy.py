class AdaptiveStrategy:

    def adapt(
        self,
        training_plan,
        comparison_report
    ):

        status = comparison_report.get(
            "status"
        )

        updated_plan = (
            training_plan.copy()
        )

        if status == "degraded":

            updated_plan["epochs"] += 5

            updated_plan[
                "learning_action"
            ] = (
                "increase_epochs"
            )

        elif status == "improved":

            updated_plan[
                "learning_action"
            ] = (
                "keep_configuration"
            )

        else:

            updated_plan[
                "learning_action"
            ] = (
                "no_change"
            )

        return updated_plan