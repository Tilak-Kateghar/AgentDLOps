class ArchitectureScorer:

    def score(self, dataset_report):

        scores = {
            "MobileNetV3": 0,
            "EfficientNetB0": 0,
            "ResNet50": 0
        }

        dataset_size = dataset_report["dataset_size"]
        num_classes = dataset_report["num_classes"]
        dataset_balance = dataset_report.get(
            "dataset_balance",
            "balanced"
        )

        # -------------------------
        # Dataset Size
        # -------------------------

        if dataset_size == "small":

            scores["MobileNetV3"] += 50
            scores["EfficientNetB0"] += 40
            scores["ResNet50"] += 20

        elif dataset_size == "medium":

            scores["MobileNetV3"] += 30
            scores["EfficientNetB0"] += 50
            scores["ResNet50"] += 45

        else:

            scores["MobileNetV3"] += 20
            scores["EfficientNetB0"] += 45
            scores["ResNet50"] += 50

        # -------------------------
        # Number of Classes
        # -------------------------

        if num_classes <= 10:

            scores["MobileNetV3"] += 20
            scores["EfficientNetB0"] += 20
            scores["ResNet50"] += 20

        elif num_classes <= 100:

            scores["EfficientNetB0"] += 25
            scores["ResNet50"] += 25

        else:

            scores["ResNet50"] += 30

        # -------------------------
        # Dataset Balance
        # -------------------------

        if dataset_balance == "balanced":

            scores["MobileNetV3"] += 10
            scores["EfficientNetB0"] += 10
            scores["ResNet50"] += 10

        else:

            scores["ResNet50"] += 15

        return scores