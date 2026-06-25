from app.core.database import (
    engine,
    Base
)

from app.models.project_run import (
    ProjectRun
)

Base.metadata.create_all(
    bind=engine
)

print(
    "PROJECT_RUNS TABLE CREATED"
)