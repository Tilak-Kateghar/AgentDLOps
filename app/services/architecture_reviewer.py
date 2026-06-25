from app.services.candidate_selector import (
    CandidateSelector
)

class ArchitectureReviewer:

    def review(
        self,
        recommendation,
        comparison_report,
        current_model=None
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

        selector = (
            CandidateSelector()
        )

        candidate = (
            selector.select_best_candidate(
                recommendation,
                current_model
            )
        )

        return {

            "selected_model":
                candidate,

            "reason":
                "performance_degraded_switch_model"
        }