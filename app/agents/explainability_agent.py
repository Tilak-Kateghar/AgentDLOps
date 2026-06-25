from app.agents.llm_architect_agent import (
    LLMArchitectAgent
)


class ExplainabilityAgent:

    def explain(
        self,
        optimization_result
    ):

        llm = (
            LLMArchitectAgent()
        )

        prompt = f"""
Explain why this architecture
was selected.

Optimization Result:

{optimization_result}

Provide:

1. Architecture rationale
2. Hyperparameter rationale
3. Deployment rationale
"""

        return llm.client.chat.completions.create(

            model=
            "llama-3.3-70b-versatile",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        ).choices[0].message.content