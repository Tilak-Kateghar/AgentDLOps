class DeploymentStrategyAgent:

    def recommend(
        self,
        intake_report,
        selected_model
    ):

        deployment = (
            intake_report[
                "deployment_target"
            ]
        )

        priority = (
            intake_report[
                "optimization_priority"
            ]
        )

        if deployment == "mobile":

            return {

                "platform":
                    "TensorFlow Lite",

                "format":
                    "tflite",

                "recommended_model":
                    "MobileNetV3",

                "reason":
                    "low_latency_mobile_inference"
            }

        elif deployment == "edge":

            return {

                "platform":
                    "ONNX Runtime",

                "format":
                    "onnx",

                "recommended_model":
                    selected_model,

                "reason":
                    "edge_optimized"
            }

        elif deployment == "cloud":

            return {

                "platform":
                    "TorchServe",

                "format":
                    "pth",

                "recommended_model":
                    selected_model,

                "reason":
                    "high_accuracy_server_inference"
            }

        return {

            "platform":
                "unknown",

            "format":
                "unknown",

            "recommended_model":
                selected_model
        }