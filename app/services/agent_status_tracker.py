from app.core.database import (
    SessionLocal
)

from app.models.agent_status import (
    AgentStatus
)


class AgentStatusTracker:

    def update(
        self,
        agent_name,
        state
    ):

        db = SessionLocal()

        row = (
            db.query(
                AgentStatus
            )
            .filter(
                AgentStatus.agent_name
                ==
                agent_name
            )
            .first()
        )

        if row:

            row.status = state

        else:

            row = AgentStatus(

                agent_name=
                agent_name,

                status=
                state
            )

            db.add(row)

        db.commit()

        db.close()

    def get_status(self):

        db = SessionLocal()

        rows = (
            db.query(
                AgentStatus
            )
            .all()
        )

        result = {}

        for row in rows:

            result[
                row.agent_name
            ] = row.status

        db.close()

        return result