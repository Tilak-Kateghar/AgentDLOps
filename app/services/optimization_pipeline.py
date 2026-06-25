# from app.agents.optimization_agent import (
#     OptimizationAgent
# )


# class OptimizationPipeline:

#     def execute(
#         self,
#         problem_type
#     ):

#         if (
#             problem_type
#             ==
#             "image_classification"
#         ):

#             candidate_models = [

#                 "EfficientNetB0",
#                 "ResNet50"
#             ]

#         else:

#             candidate_models = []

#         optimizer = (
#             OptimizationAgent()
#         )

#         result = (
#             optimizer.optimize(
#                 candidate_models
#             )
#         )

#         return result

from app.agents.optimization_agent import (
    OptimizationAgent
)

from app.agents.candidate_family_agent import (
    CandidateFamilyAgent
)

from app.services.model_validator import (
    ModelValidator
)


class OptimizationPipeline:

    def execute(
        self,
        intake_report
    ):

        candidate_agent = (
            CandidateFamilyAgent()
        )

        candidate_result = (
            candidate_agent.recommend(
                intake_report
            )
        )

        candidate_models = (
            ModelValidator.validate(

                candidate_result[
                    "candidates"
                ]
            )
        )

        if len(
            candidate_models
        ) == 0:

            candidate_models = [
                "ResNet50"
            ]

        optimizer = (
            OptimizationAgent()
        )

        optimization_result = (
            optimizer.optimize(
                candidate_models
            )
        )

        optimization_result[
            "candidate_result"
        ] = candidate_result

        return optimization_result