# class AutonomousDeploymentAgent:

#     def recommend(
#         self,
#         intake_report,
#         optimization_result
#     ):

#         deployment_target = (
#             intake_report.get(
#                 "deployment_target",
#                 "cloud"
#             )
#         )

#         best_model = (
#             optimization_result[
#                 "best_architecture"
#             ][
#                 "model"
#             ]
#         )

#         if deployment_target == "mobile":

#             return {

#                 "model":
#                     best_model,

#                 "deployment_platform":
#                     "TensorFlow Lite",

#                 "artifact":
#                     ".tflite",

#                 "reason":
#                     "Optimized for mobile inference"
#             }

#         elif deployment_target == "edge":

#             return {

#                 "model":
#                     best_model,

#                 "deployment_platform":
#                     "ONNX Runtime",

#                 "artifact":
#                     ".onnx",

#                 "reason":
#                     "Lightweight edge deployment"
#             }

#         elif deployment_target == "web_api":

#             return {

#                 "model":
#                     best_model,

#                 "deployment_platform":
#                     "FastAPI",

#                 "artifact":
#                     ".pth",

#                 "reason":
#                     "REST inference service"
#             }

#         else:

#             return {

#                 "model":
#                     best_model,

#                 "deployment_platform":
#                     "TorchServe",

#                 "artifact":
#                     ".pth",

#                 "reason":
#                     "Cloud deployment"
#             }

from app.services.deployment_recommender import (
    DeploymentRecommender
)


class AutonomousDeploymentAgent:

    def recommend(
        self,
        intake_report,
        optimization_result
    ):

        best_model = (

            optimization_result[
                "best_architecture"
            ][
                "model"
            ]
        )

        recommender = (
            DeploymentRecommender()
        )

        deployment = (
            recommender.recommend(
                intake_report,
                best_model
            )
        )

        deployment[
            "model"
        ] = best_model

        return deployment