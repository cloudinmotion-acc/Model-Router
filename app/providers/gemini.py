import os
import asyncio
from google.genai import Client
from .base import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        api_key = os.getenv("API_KEY")
        self.client = Client(api_key=api_key)

    async def generate(self, prompt: str, model: str, parameters: dict, state: dict = None): # type: ignore
        state = state or {}
        messages = state.get("history", [])
        
        # If no history, just use the current prompt
        if not messages:
            messages = [{"role": "user", "parts": [{"text": prompt}]}]
        else:
            # Append current prompt to history
            messages = messages + [{"role": "user", "parts": [{"text": prompt}]}]
        
        # Set default parameters if not provided
        if "max_output_tokens" not in parameters:
            parameters["max_output_tokens"] = 1024
        
        # Run the synchronous API call in a thread pool for async compatibility
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: self.client.models.generate_content(
                model=model,
                contents=messages,
                config=parameters
            )
        )

        return {
            "text": response.text,
            "model": model,
            "usage": {
                "input_tokens": response.usage_metadata.prompt_token_count if response.usage_metadata else 0,
                "output_tokens": response.usage_metadata.candidates_token_count if response.usage_metadata else 0
            }
        }
