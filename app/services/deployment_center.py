class DeploymentCenter:

    def build_report(
        self,
        deployment_result,
        cost_result
    ):

        return {

            "model":
                deployment_result[
                    "model"
                ],

            "platform":
                deployment_result[
                    "deployment_platform"
                ],

            "artifact":
                deployment_result[
                    "artifact"
                ],

            "status":
                "Ready",

            "monthly_cost":
                cost_result[
                    "monthly_cost_usd"
                ]
        }