class HyperparameterSelector:

    def select_best_trial(
        self,
        trial_results
    ):

        return max(
            trial_results,
            key=lambda x: x["accuracy"]
        )