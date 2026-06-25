class ChampionChallengerAgent:

    def evaluate(
        self,
        champion_accuracy,
        challenger_accuracy,
        minimum_gain=1.0
    ):

        improvement = (

            challenger_accuracy
            -
            champion_accuracy
        )

        promote = (
            improvement >= minimum_gain
        )

        return {

            "champion_accuracy":
                champion_accuracy,

            "challenger_accuracy":
                challenger_accuracy,

            "improvement":
                round(
                    improvement,
                    2
                ),

            "promote":
                promote
        }