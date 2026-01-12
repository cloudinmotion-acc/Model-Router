import os
from openai import AsyncOpenAI
from .base import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    async def generate(self, prompt: str, model: str, parameters: dict):
        response = await self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **parameters
        )

        return {
            "text": response.choices[0].message.content,
            "model": model,
            "usage": response.usage.model_dump()
        }
