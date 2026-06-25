import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LLMControllerAgent:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            )
        )

    def decide(
        self,
        system_state
    ):

        prompt = f"""
You are the Chief AI Officer of AgentDLOps.

Current System State:

{json.dumps(system_state, indent=2)}

Available Actions:

1. architecture_search
2. optimize_model
3. deploy_model
4. rollback_model
5. retrain_model
6. monitor_only

Choose exactly ONE action.

Return JSON only:

{{
  "action": "...",
  "reason": "..."
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

        return (
            response
            .choices[0]
            .message.content
        )

    def decide_and_execute(
        self,
        system_state,
        tool_registry
    ):

        decision = (
            self.decide(
                system_state
            )
        )

        try:

            decision_json = (
                json.loads(
                    decision
                )
            )

        except Exception:

            decision_json = {

                "action":
                    "monitor_only",

                "reason":
                    "Failed to parse LLM response"
            }

        execution = (

            tool_registry.execute(

                decision_json[
                    "action"
                ]
            )
        )

        return {

            "decision":
                decision_json,

            "execution":
                execution
        }