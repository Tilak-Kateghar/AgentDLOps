from app.models.training_status import (
    TrainingStatus
)

from app.core.database import (
    Base,
    engine
)

Base.metadata.create_all(
    bind=engine
)

print(
    "TRAINING STATUS TABLE CREATED"
)