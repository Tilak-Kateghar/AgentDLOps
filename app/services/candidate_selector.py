class CandidateSelector:

    def select_best_candidate(
        self,
        recommendation,
        current_model
    ):

        candidates = (
            recommendation[
                "recommended_models"
            ]
        )

        for model in candidates:

            if model != current_model:

                return model

        return current_model