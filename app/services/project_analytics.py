from sqlalchemy import func

from app.core.database import (
    SessionLocal
)

from app.models.project_run import (
    ProjectRun
)


class ProjectAnalytics:

    def get_statistics(
        self
    ):

        db = SessionLocal()

        total_runs = (
            db.query(
                ProjectRun
            ).count()
        )

        best_accuracy = (
            db.query(
                func.max(
                    ProjectRun.accuracy
                )
            ).scalar()
        )

        rows = (
            db.query(
                ProjectRun
            ).all()
        )

        architecture_usage = {}

        for row in rows:

            architecture = (
                row.architecture
            )

            architecture_usage[
                architecture
            ] = (
                architecture_usage.get(
                    architecture,
                    0
                ) + 1
            )

        db.close()

        return {

            "total_runs":
                total_runs,

            "best_accuracy":
                best_accuracy,

            "architecture_usage":
                architecture_usage
        }