import json
import os
from datetime import datetime


class ModelLineageAgent:

    def save(
        self,
        intake_report,
        optimization_result,
        deployment_result
    ):

        os.makedirs(
            "lineage",
            exist_ok=True
        )

        lineage = {

            "timestamp":
                str(datetime.now()),

            "project":

                intake_report,

            "architecture":

                optimization_result[
                    "best_architecture"
                ],

            "hyperparameters":

                optimization_result[
                    "best_hyperparameter"
                ],

            "deployment":

                deployment_result
        }

        path = (
            "lineage/"
            "model_lineage.json"
        )

        with open(
            path,
            "w"
        ) as file:

            json.dump(
                lineage,
                file,
                indent=4
            )

        return path