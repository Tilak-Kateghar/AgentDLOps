class ConsensusAgent:

    def decide(
        self,
        llm_choice,
        benchmark_choice
    ):

        scores = {}

        scores[llm_choice] = (
            scores.get(
                llm_choice,
                0
            ) + 0.4
        )

        scores[benchmark_choice] = (
            scores.get(
                benchmark_choice,
                0
            ) + 0.6
        )

        winner = max(
            scores,
            key=scores.get
        )

        return {

            "selected_model":
                winner,

            "scores":
                scores
        }