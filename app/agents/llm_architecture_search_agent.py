import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LLMArchitectureSearchAgent:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def search(
        self,
        project_context
    ):

        prompt = f"""
You are a Deep Learning Architecture Expert.

Project Context:

{json.dumps(project_context, indent=2)}

Recommend:

1. Best architecture family
2. Candidate models
3. Why this family is suitable
4. Estimated deployment suitability

Return JSON only.

Example:

{{
    "family":"EfficientNet",

    "candidates":[
        "EfficientNetB0",
        "EfficientNetB3"
    ],

    "reason":"Mobile deployment with strong accuracy",

    "deployment":"TensorFlow Lite"
}}
"""

        response = (
            self.client.chat.completions.create(

                model=
                "llama-3.3-70b-versatile",

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