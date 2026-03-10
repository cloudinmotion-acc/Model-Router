import os
import google.generativeai as genai
from .base import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.client = genai.GenerativeModel

    async def generate(self, prompt: str, model: str, parameters: dict, state: dict = None): # type: ignore
        state = state or {}
        messages = state.get("history", [])
        
        # If no history, just use the current prompt
        if not messages:
            messages = [{"role": "user", "parts": [{"text": prompt}]}]
        
        # Initialize Gemini model
        model_instance = self.client(model_name=model)
        
        # Create chat session
        chat_session = model_instance.start_chat(history=messages)
        
        response = await chat_session.send_message_async(
            prompt,
            **parameters
        )

        return {
            "text": response.text,
            "model": model,
            "usage": {
                "prompt_tokens": response.usage_metadata.prompt_token_count,
                "completion_tokens": response.usage_metadata.candidates_token_count
            }
        }
