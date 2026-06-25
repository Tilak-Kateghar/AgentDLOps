import json

from app.services.vector_memory import (
    VectorMemory
)

from app.agents.llm_controller_agent import (
    LLMControllerAgent
)


class MemoryPlannerAgent:

    def plan(
        self,
        system_state
    ):

        memory = (
            VectorMemory()
        )

        query = (
            system_state.get(
                "problem_type",
                "image_classification"
            )
        )

        results = (
            memory.search(
                query
            )
        )

        documents = (
            results.get(
                "documents",
                [[]]
            )[0]
        )

        memory_context = "\n".join(
            documents
        )

        controller = (
            LLMControllerAgent()
        )

        enhanced_state = {

            "current_state":
                system_state,

            "historical_memory":
                memory_context
        }

        return (
            controller.decide(
                enhanced_state
            )
        )