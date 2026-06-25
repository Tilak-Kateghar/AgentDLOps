import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LLMArchitectAgent:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def recommend(
        self,
        intake_report,
        retrieved_context=""
    ):

        prompt = f"""
You are a Senior AI Architect.

Historical Successful Projects:

{retrieved_context}

Current Project:

{intake_report}

Recommend:

1. Architecture Family
2. Candidate Models
3. Deployment Strategy

Return ONLY valid JSON.

Example:

{{
    "family":"ResNet",
    "candidates":[
        "ResNet18",
        "ResNet34",
        "ResNet50"
    ],
    "deployment_strategy": {{
        "model_pruning": true,
        "quantization": true,
        "knowledge_distillation": true,
        "optimization_technique": "latency_optimization"
    }}
}}
"""

        response = (
            self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        content = (
            response
            .choices[0]
            .message
            .content
        )

        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(content)