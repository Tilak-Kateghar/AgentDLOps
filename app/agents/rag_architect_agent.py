from app.services.vector_memory import (
    VectorMemory
)

from app.agents.llm_architect_agent import (
    LLMArchitectAgent
)


class RAGArchitectAgent:

    def recommend(
        self,
        intake_report
    ):

        memory = (
            VectorMemory()
        )

        query = f"""
        {intake_report['problem_type']}
        {intake_report['dataset_type']}
        {intake_report['deployment_target']}
        {intake_report['optimization_priority']}
        """

        memory_result = (
            memory.search(
                query
            )
        )

        docs = (
            memory_result.get(
                "documents",
                [[]]
            )[0]
        )

        context = "\n".join(
            docs
        )

        architect = (
            LLMArchitectAgent()
        )

        return architect.recommend(
            intake_report,
            context
        )