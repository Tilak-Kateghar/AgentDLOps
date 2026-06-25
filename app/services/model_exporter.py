import os
import torch

class ModelExporter:

    def __init__(self):

        self.export_dir = "exports"

        os.makedirs(
            self.export_dir,
            exist_ok=True
        )

    def export_pytorch(
        self,
        model,
        model_name
    ):

        path = (
            f"{self.export_dir}/"
            f"{model_name}.pth"
        )

        torch.save(
            model.state_dict(),
            path
        )

        return path