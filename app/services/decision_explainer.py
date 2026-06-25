class DecisionExplainer:

    def explain_architecture_choice(
        self,
        benchmark_results,
        winner
    ):

        explanation = (
            f"{winner['model']} selected "
            f"because it achieved "
            f"{winner['accuracy']:.2f}% "
            f"accuracy, which was the "
            f"highest among all "
            f"candidate architectures."
        )

        return explanation

    def explain_hyperparameter_choice(
        self,
        winner
    ):

        explanation = (
            f"Learning rate "
            f"{winner['learning_rate']} "
            f"selected because it "
            f"produced the highest "
            f"accuracy of "
            f"{winner['accuracy']:.2f}%."
        )

        return explanation