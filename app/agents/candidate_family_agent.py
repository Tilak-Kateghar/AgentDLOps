from app.agents.rag_architect_agent import (
    RAGArchitectAgent
)


class CandidateFamilyAgent:

    def recommend(
        self,
        intake_report
    ):

        rag_agent = (
            RAGArchitectAgent()
        )

        return (
            rag_agent.recommend(
                intake_report
            )
        )