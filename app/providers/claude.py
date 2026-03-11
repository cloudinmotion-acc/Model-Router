import os
from anthropic import AsyncAnthropic
from .base import BaseProvider


class ClaudeProvider(BaseProvider):

    def __init__(self):
        self.client = AsyncAnthropic(api_key=os.getenv("API_KEY"))

    async def generate(self, prompt: str, model: str, parameters: dict, state: dict = None): # type: ignore
        state = state or {}
        messages = state.get("history", [])
        
        # If no history, just use the current prompt
        if not messages:
            messages = [{"role": "user", "content": prompt}]
        
        # Set default max_tokens if not provided
        if "max_tokens" not in parameters:
            parameters["max_tokens"] = 1024
        
        response = await self.client.messages.create(
            model=model,
            messages=messages,
            **parameters
        )

        return {
            "text": response.content[0].text,
            "model": model,
            "usage": {
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens
            }
        }
        
