import json
import os


class DashboardDataProvider:

    def load_best_model(self):

        path = "reports/best_model.json"

        if not os.path.exists(path):
            return {}

        with open(path, "r") as file:
            return json.load(file)

    def load_run_history(self):

        path = "reports/run_history.json"

        if not os.path.exists(path):
            return []

        with open(path, "r") as file:
            return json.load(file)

    def load_decision_report(self):

        path = (
            "reports/final_decision_report.json"
        )

        if not os.path.exists(path):
            return {}

        with open(path, "r") as file:
            return json.load(file)