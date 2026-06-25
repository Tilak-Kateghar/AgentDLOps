from app.models.agent_status import (
    AgentStatus
)

from app.core.base import Base
from app.core.database import engine

Base.metadata.create_all(
    bind=engine
)

print(
    "AGENT STATUS TABLE CREATED"
)