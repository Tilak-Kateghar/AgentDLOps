class DeploymentCostAgent:

    def estimate(
        self,
        model_name
    ):

        costs = {

            "ResNet18": 12,

            "ResNet34": 18,

            "ResNet50": 25,

            "EfficientNetB0": 15,

            "MobileNetV3": 8
        }

        monthly_cost = (
            costs.get(
                model_name,
                10
            )
        )

        return {

            "model":
                model_name,

            "monthly_cost_usd":
                monthly_cost
        }