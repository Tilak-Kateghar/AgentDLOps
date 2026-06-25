class ModelValidator:

    SUPPORTED_MODELS = [

        "ResNet18",

        "ResNet34",

        "ResNet50",

        "EfficientNetB0",

        "MobileNetV3"
    ]

    @staticmethod
    def validate(
        candidate_models
    ):

        valid_models = []

        for model in candidate_models:

            if (
                model
                in
                ModelValidator
                .SUPPORTED_MODELS
            ):

                valid_models.append(
                    model
                )

        return valid_models