from app.services.best_model_manager import (
    BestModelManager
)


class ChampionManager:

    def evaluate_candidate(
        self,
        accuracy,
        model_name
    ):

        manager = (
            BestModelManager()
        )

        if manager.is_new_best(
            accuracy
        ):

            manager.update_best_accuracy(
                accuracy,
                model_name
            )

            return {

                "status":
                    "promoted",

                "best_accuracy":
                    accuracy,

                "best_model":
                    model_name
            }

        return {

            "status":
                "rejected",

            "best_accuracy":
                manager.get_best_accuracy(),

            "best_model":
                manager.get_best_model()
        }