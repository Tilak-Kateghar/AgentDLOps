import json
import os


class ReportExporter:

    def __init__(self):

        self.report_dir = (
            "reports"
        )

        os.makedirs(
            self.report_dir,
            exist_ok=True
        )

    def export_json(
        self,
        report,
        filename
    ):

        path = (
            f"{self.report_dir}/"
            f"{filename}.json"
        )

        with open(
            path,
            "w"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        return path