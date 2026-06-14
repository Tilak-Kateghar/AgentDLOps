from app.models.model_factory import (
    ModelFactory
)

from app.services.model_registry import (
    ModelRegistry
)


def main():

    model = ModelFactory.create_model(
        "EfficientNetB0",
        num_classes=10
    )

    registry = ModelRegistry()

    path = registry.save_best_model(
        model,
        "EfficientNetB0"
    )

    print(
        "\nBEST MODEL REPORT"
    )

    print("=" * 40)

    print(
        f"saved_model: {path}"
    )


if __name__ == "__main__":
    main()