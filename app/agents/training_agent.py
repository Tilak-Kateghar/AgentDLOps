import torch
from app.services.dataset_loader import (
    DatasetLoader
)
from app.services.training_executor import (
    TrainingExecutor
)
from app.models.model_factory import ModelFactory
from app.services.training_configurator import (
    TrainingConfigurator
)
from app.services.model_registry import (
    ModelRegistry
)

class TrainingAgent:
    """
    Training Agent

    Receives architecture recommendations
    and prepares training plans.
    """

    def create_training_plan(
        self,
        recommendation,
        dataset_report
    ):

        selected_model = recommendation[
            "recommended_models"
        ][0]

        model = ModelFactory.create_model(
            selected_model
        )

        configurator = TrainingConfigurator()

        config = configurator.generate_config(
            dataset_report,
            selected_model
        )

        training_plan = {
            "selected_model": selected_model,
            "model_type": type(model).__name__,
            "epochs": config["epochs"],
            "batch_size": config["batch_size"],
            "optimizer": config["optimizer"]
        }

        return training_plan
    
    def execute_training(
        self,
        dataset_report,
        recommendation
    ):

        plan = self.create_training_plan(
            recommendation,
            dataset_report
        )

        model = ModelFactory.create_model(
            plan["selected_model"],
            num_classes=10
        )

        loader = DatasetLoader()

        train_loader, test_loader = (
            loader.load_cifar10(
                batch_size=plan["batch_size"]
            )
        )

        optimizer = torch.optim.Adam(
            model.parameters(),
            lr=0.001
        )

        criterion = (
            torch.nn.CrossEntropyLoss()
        )

        executor = TrainingExecutor()

        epoch_history = (
            executor.train_multiple_epochs(
                model,
                train_loader,
                optimizer,
                criterion,
                plan["epochs"]
            )
        )

        final_result = {
            "average_loss":
                epoch_history[-1]["loss"],

            "epochs_trained":
                len(epoch_history)
        }

        registry = ModelRegistry()

        model_path = registry.save_model(
            model,
            plan["selected_model"]
        )

        return {

            "training_plan":
                plan,

            "training_result":
                final_result,

            "epoch_history":
                epoch_history,

            "trained_model":
                model,

            "test_loader":
                test_loader,

            "model_path":
                model_path
        }