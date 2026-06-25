class DeploymentRecommender:

    def recommend(
        self,
        intake_report,
        best_model
    ):

        target = (
            intake_report.get(
                "deployment_target",
                "cloud"
            )
        )

        priority = (
            intake_report.get(
                "optimization_priority",
                "accuracy"
            )
        )

        # --------------------------
        # Mobile
        # --------------------------

        if target == "mobile":

            return {

                "platform":
                    "TensorFlow Lite",

                "artifact":
                    ".tflite",

                "optimization":
                    [
                        "quantization",
                        "pruning"
                    ],

                "reason":
                    "Mobile deployment"
            }

        # --------------------------
        # Edge
        # --------------------------

        if target == "edge":

            return {

                "platform":
                    "ONNX Runtime",

                "artifact":
                    ".onnx",

                "optimization":
                    [
                        "quantization"
                    ],

                "reason":
                    "Edge inference"
            }

        # --------------------------
        # Low Cost Cloud
        # --------------------------

        if priority == "cost":

            return {

                "platform":
                    "FastAPI",

                "artifact":
                    ".pth",

                "optimization":
                    [
                        "cpu_inference"
                    ],

                "reason":
                    "Cost optimized"
            }

        # --------------------------
        # High Accuracy Cloud
        # --------------------------

        return {

            "platform":
                "TorchServe",

            "artifact":
                ".pth",

            "optimization":
                [
                    "gpu_inference"
                ],

            "reason":
                "Maximum accuracy"
        }