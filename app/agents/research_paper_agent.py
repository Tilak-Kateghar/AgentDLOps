import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class ResearchPaperAgent:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def generate(
        self,
        project_data
    ):

        prompt = f"""
Generate a research paper draft.

Project Information:

{project_data}

Include:

1. Abstract
2. Introduction
3. Methodology
4. Results
5. Conclusion

Return markdown format.
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

        return (
            response
            .choices[0]
            .message.content
        )