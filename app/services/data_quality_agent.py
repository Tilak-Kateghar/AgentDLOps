class DataQualityAgent:

    def analyze(
        self,
        dataset_report
    ):

        report = {

            "dataset_name":
                dataset_report.get(
                    "dataset_name"
                ),

            "total_images":
                dataset_report.get(
                    "total_images"
                ),

            "num_classes":
                dataset_report.get(
                    "num_classes"
                ),

            "quality_status":
                "good"
        }

        if (
            dataset_report[
                "total_images"
            ] < 1000
        ):

            report[
                "quality_status"
            ] = "low_data"

        return report