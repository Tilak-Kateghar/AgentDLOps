import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class DebateAgent:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def debate(
        self,
        architect_view,
        optimization_view,
        deployment_view
    ):

        prompt = f"""
You are an AI Judge.

Three expert agents disagree.

Architect Agent:

{architect_view}

Optimization Agent:

{optimization_view}

Deployment Agent:

{deployment_view}

Choose the best recommendation.

Return JSON only:

{{
    "winner":"...",
    "reason":"..."
}}
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