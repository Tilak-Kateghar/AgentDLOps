import json
import os


class RunHistory:

    def __init__(self):

        self.history_file = (
            "reports/run_history.json"
        )

    def save_run(self, report):

        history = []

        if os.path.exists(
            self.history_file
        ):

            with open(
                self.history_file,
                "r"
            ) as file:

                history = json.load(
                    file
                )

        history.append(report)

        with open(
            self.history_file,
            "w"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )

    def load_history(self):

        if not os.path.exists(
            self.history_file
        ):

            return []

        with open(
            self.history_file,
            "r"
        ) as file:

            return json.load(
                file
            )