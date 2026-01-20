import os
from openai import AsyncOpenAI
from .base import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY")) # type: ignore # 

    async def generate(self, prompt: str, model: str, parameters: dict, state: dict = None): # type: ignore
        state = state or {}
        messages = state.get("history", [])
        
        # If no history, just use the current prompt
        if not messages:
            messages = [{"role": "user", "content": prompt}]
        
        response = await self.client.chat.completions.create(
            model=model,
            messages=messages,
            **parameters
        )

        return {
            "text": response.choices[0].message.content,
            "model": model,
            "usage": response.usage.model_dump()
        }
