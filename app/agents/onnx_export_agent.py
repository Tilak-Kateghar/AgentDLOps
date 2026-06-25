import os
import torch


class ONNXExportAgent:

    def export(
        self,
        model,
        model_name
    ):

        os.makedirs(
            "deployment",
            exist_ok=True
        )

        path = (
            f"deployment/{model_name}.onnx"
        )

        model.eval()

        dummy_input = torch.randn(
            1,
            3,
            32,
            32
        )

        torch.onnx.export(
            model,
            dummy_input,
            path,
            export_params=True,
            opset_version=18,
            dynamo=False
        )

        return {
            "artifact": path
        }