from torchvision.models import (
    mobilenet_v3_small,
    efficientnet_b0,
    resnet50
)

import torch.nn as nn


class ModelFactory:

    @staticmethod
    def create_model(
        model_name,
        num_classes=10
    ):

        if model_name == "MobileNetV3":

            model = mobilenet_v3_small()

            in_features = (
                model.classifier[3].in_features
            )

            model.classifier[3] = nn.Linear(
                in_features,
                num_classes
            )

            return model

        elif model_name == "EfficientNetB0":

            model = efficientnet_b0()

            in_features = (
                model.classifier[1].in_features
            )

            model.classifier[1] = nn.Linear(
                in_features,
                num_classes
            )

            return model

        elif model_name == "ResNet50":

            model = resnet50()

            in_features = model.fc.in_features

            model.fc = nn.Linear(
                in_features,
                num_classes
            )

            return model

        else:

            raise ValueError(
                f"Unsupported model: {model_name}"
            )