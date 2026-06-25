import json
import os


class SelfImprovingAgent:

    def __init__(self):

        self.file = (
            "memory/self_improvement.json"
        )

        os.makedirs(
            "memory",
            exist_ok=True
        )

    def learn(
        self,
        decision,
        outcome
    ):

        record = {

            "decision":
                decision,

            "outcome":
                outcome
        }

        history = []

        if os.path.exists(
            self.file
        ):

            with open(
                self.file,
                "r"
            ) as f:

                history = json.load(
                    f
                )

        history.append(
            record
        )

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                history,
                f,
                indent=4
            )

        return {

            "status":
                "Learning Saved",

            "total_memories":
                len(history)
        }