from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


class PDFReportGenerator:

    def generate(
        self,
        intake_report,
        optimization_result,
        deployment_result=None,
        output_path=
        "reports/AgentDLOps_Report.pdf"
    ):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        document = (
            SimpleDocTemplate(
                output_path
            )
        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        # --------------------------------
        # Title
        # --------------------------------

        elements.append(
            Paragraph(
                "AgentDLOps Optimization Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # --------------------------------
        # Project Intake
        # --------------------------------

        elements.append(
            Paragraph(
                "Project Intake",
                styles["Heading1"]
            )
        )

        for key, value in (
            intake_report.items()
        ):

            elements.append(

                Paragraph(
                    f"<b>{key}</b>: {value}",
                    styles["BodyText"]
                )
            )

        elements.append(
            Spacer(1, 12)
        )

        # --------------------------------
        # Architecture
        # --------------------------------

        elements.append(
            Paragraph(
                "Best Architecture",
                styles["Heading1"]
            )
        )

        best_arch = (
            optimization_result[
                "best_architecture"
            ]
        )

        elements.append(

            Paragraph(
                str(best_arch),
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

        # --------------------------------
        # Hyperparameters
        # --------------------------------

        elements.append(
            Paragraph(
                "Best Hyperparameters",
                styles["Heading1"]
            )
        )

        best_hp = (
            optimization_result[
                "best_hyperparameter"
            ]
        )

        elements.append(

            Paragraph(
                str(best_hp),
                styles["BodyText"]
            )
        )

        elements.append(
            Spacer(1, 12)
        )

        # --------------------------------
        # Deployment
        # --------------------------------

        if deployment_result:

            elements.append(
                Paragraph(
                    "Deployment Recommendation",
                    styles["Heading1"]
                )
            )

            elements.append(

                Paragraph(
                    str(deployment_result),
                    styles["BodyText"]
                )
            )

        elements.append(
            PageBreak()
        )

        # --------------------------------
        # Summary
        # --------------------------------

        elements.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        summary = f"""
        Selected Architecture:
        {best_arch['model']} <br/>

        Architecture Accuracy:
        {best_arch['accuracy']} <br/>

        Learning Rate:
        {best_hp['learning_rate']} <br/>

        Batch Size:
        {best_hp['batch_size']}
        """

        elements.append(

            Paragraph(
                summary,
                styles["BodyText"]
            )
        )

        document.build(
            elements
        )

        return output_path