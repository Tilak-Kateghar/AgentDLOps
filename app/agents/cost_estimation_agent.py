class CostEstimationAgent:

    def estimate(
        self,
        deployment_result
    ):

        platform = (
            deployment_result[
                "deployment_platform"
            ]
        )

        costs = {

            "TensorFlow Lite": 0,
            "ONNX Runtime": 5,
            "FastAPI": 20,
            "TorchServe": 40
        }

        return {

            "platform":
                platform,

            "estimated_monthly_cost":
                costs.get(
                    platform,
                    10
                )
        }