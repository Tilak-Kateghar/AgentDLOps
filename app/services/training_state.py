from app.core.database import (
    SessionLocal
)

from app.models.training_status import (
    TrainingStatus
)


class TrainingState:

    def update(
        self,
        model,
        epoch,
        loss,
        accuracy,
        status
    ):

        db = SessionLocal()

        row = (
            db.query(
                TrainingStatus
            )
            .first()
        )

        if row:

            row.model = model
            row.epoch = epoch
            row.loss = float(loss)
            row.accuracy = float(accuracy)
            row.status = status

        else:

            row = TrainingStatus(

                model=model,
                epoch=epoch,
                loss=float(loss),
                accuracy=float(accuracy),
                status=status
            )

            db.add(row)

        db.commit()
        db.close()

    def get_state(self):

        db = SessionLocal()

        row = (
            db.query(
                TrainingStatus
            )
            .first()
        )

        db.close()

        if not row:

            return {
                "model": None,
                "epoch": 0,
                "loss": 0,
                "accuracy": 0,
                "status": "Idle"
            }

        return {

            "model":
                row.model,

            "epoch":
                row.epoch,

            "loss":
                row.loss,

            "accuracy":
                row.accuracy,

            "status":
                row.status
        }