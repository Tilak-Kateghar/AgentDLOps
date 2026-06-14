from app.models.model_factory import (
    ModelFactory
)

from app.services.model_registry import (
    ModelRegistry
)


def main():

    model = (
        ModelFactory.create_model(
            "EfficientNetB0",
            num_classes=10
        )
    )

    registry = ModelRegistry()

    model_path = (
        registry.save_model(
            model,
            "efficientnet_test"
        )
    )

    print(
        "\nMODEL REGISTRY REPORT"
    )

    print("=" * 40)

    print(
        f"saved_model: {model_path}"
    )


if __name__ == "__main__":
    main()