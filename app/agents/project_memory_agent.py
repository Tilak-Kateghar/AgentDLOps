from app.services.vector_memory import (
    VectorMemory
)

class ProjectMemoryAgent:

    def retrieve_context(
        self,
        query
    ):

        memory = VectorMemory()

        result = memory.search(
            query
        )

        try:

            return "\n".join(
                result["documents"][0]
            )

        except:

            return ""