import os
import torch


class ModelRegistry:

    def __init__(self):

        self.registry_path = (
            "saved_models"
        )

        os.makedirs(
            self.registry_path,
            exist_ok=True
        )

    def save_model(
        self,
        model,
        model_name
    ):

        model_path = (
            f"{self.registry_path}/"
            f"{model_name}.pth"
        )

        torch.save(
            model.state_dict(),
            model_path
        )

        return model_path

    def save_best_model(
        self,
        model,
        model_name
    ):

        model_path = (
            f"{self.registry_path}/"
            f"best_{model_name}.pth"
        )

        torch.save(
            model.state_dict(),
            model_path
        )

        return model_path