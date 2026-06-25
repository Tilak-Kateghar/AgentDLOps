import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class CloudDeploymentPlannerAgent:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def plan(
        self,
        deployment_context
    ):

        prompt = f"""
You are a Cloud MLOps Architect.

Context:

{json.dumps(deployment_context, indent=2)}

Choose:

1. Cloud Provider
2. Training Platform
3. Deployment Platform
4. Instance Type
5. Estimated Cost

Return JSON only.
"""

        response = (
            self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message.content
        )