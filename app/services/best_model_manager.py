import json
import os


class BestModelManager:

    def __init__(self):

        self.file_path = (
            "reports/best_model.json"
        )

    def get_best_accuracy(self):

        if not os.path.exists(
            self.file_path
        ):

            return 0

        with open(
            self.file_path,
            "r"
        ) as file:

            data = json.load(file)

        return data["best_accuracy"]

    def update_best_accuracy(
        self,
        accuracy,
        model_name
    ):

        data = {

            "best_accuracy":
                accuracy,

            "best_model":
                model_name
        }

        with open(
            self.file_path,
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def is_new_best(
        self,
        accuracy
    ):

        current_best = (
            self.get_best_accuracy()
        )

        return accuracy > current_best
    
    def get_best_model(self):

        if not os.path.exists(
            self.file_path
        ):
            return None

        with open(
            self.file_path,
            "r"
        ) as file:

            data = json.load(file)

        return data["best_model"]