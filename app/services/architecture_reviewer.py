class ArchitectureReviewer:

    def review(
        self,
        recommendation,
        comparison_report
    ):

        ranked_models = recommendation[
            "recommended_models"
        ]

        status = comparison_report.get(
            "status"
        )

        if status != "degraded":

            return {
                "selected_model":
                    ranked_models[0],

                "reason":
                    "keep_current_model"
            }

        if len(ranked_models) < 2:

            return {
                "selected_model":
                    ranked_models[0],

                "reason":
                    "no_alternative_available"
            }

        return {

            "selected_model":
                ranked_models[1],

            "reason":
                "performance_degraded_switch_model"
        }