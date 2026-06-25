class ResearchBenchmarkAgent:

    def benchmark(
        self,
        model_name,
        accuracy
    ):

        sota = {

            "ResNet18": 69.7,
            "ResNet34": 73.3,
            "ResNet50": 76.1,
            "EfficientNetB0": 77.1,
            "MobileNetV3": 75.2
        }

        target = (
            sota.get(
                model_name,
                0
            )
        )

        gap = (
            target - accuracy
        )

        return {

            "model":
                model_name,

            "your_accuracy":
                accuracy,

            "sota_accuracy":
                target,

            "gap":
                round(gap, 2)
        }