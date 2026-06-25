import json
import os


class OptimizationReportManager:

    def save(
        self,
        result
    ):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        with open(

            "reports/"
            "optimization_report.json",

            "w"

        ) as file:

            json.dump(
                result,
                file,
                indent=4
            )