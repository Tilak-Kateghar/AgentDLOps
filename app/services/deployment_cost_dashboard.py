class DeploymentCostDashboard:

    def get_cost_report(self):

        return [

            {
                "model": "ResNet18",
                "monthly_cost": 10
            },

            {
                "model": "ResNet34",
                "monthly_cost": 18
            },

            {
                "model": "ResNet50",
                "monthly_cost": 25
            },

            {
                "model": "EfficientNetB0",
                "monthly_cost": 22
            }
        ]