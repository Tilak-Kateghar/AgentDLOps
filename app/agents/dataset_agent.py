from app.services.cifar10_profiler import (
    CIFAR10Profiler
)
import json


class DatasetAgent:
    """
    Dataset Agent

    Analyzes datasets and generates
    intelligence reports.
    """

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

    def detect_balance(self, distribution):
        """
        Detects dataset imbalance.
        """

        counts = list(distribution.values())

        largest = max(counts)
        smallest = min(counts)

        ratio = largest / smallest

        if ratio <= 2:
            return "balanced"

        return "imbalanced"

    # def analyze(self):

    #     profiler = DatasetProfiler(self.dataset_path)

    #     report = profiler.generate_report()

    #     total_images = report["total_images"]

    #     if total_images < 10000:
    #         dataset_size = "small"

    #     elif total_images < 100000:
    #         dataset_size = "medium"

    #     else:
    #         dataset_size = "large"

    #     balance_status = self.detect_balance(
    #         report["class_distribution"]
    #     )

    #     intelligence_report = {
    #         "dataset_path": report["dataset_path"],
    #         "num_classes": report["num_classes"],
    #         "total_images": report["total_images"],
    #         "dataset_size": dataset_size,
    #         "class_distribution": report["class_distribution"],
    #         "dataset_balance": balance_status
    #     }

    #     return intelligence_report

    def analyze(self):

        profiler = CIFAR10Profiler()

        report = profiler.profile()

        if report["total_images"] < 10000:

            dataset_size = "small"

        elif report["total_images"] < 100000:

            dataset_size = "medium"

        else:

            dataset_size = "large"

        report["dataset_size"] = (
            dataset_size
        )

        return report

    def save_report(
        self,
        report,
        output_path="reports/dataset_report.json"
    ):

        with open(output_path, "w") as file:
            json.dump(report, file, indent=4)

        return output_path