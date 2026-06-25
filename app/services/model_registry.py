import os
import torch

from app.agents.storage_agent import (
    StorageAgent
)

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

        # storage = StorageAgent()

        # storage.upload_file(
        #     bucket="models",
        #     local_file_path=model_path
        # )

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