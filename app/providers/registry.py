from app.providers.openai import OpenAIProvider
from app.providers.claude import ClaudeProvider
from app.providers.gemini import GeminiProvider

def get_provider(name: str):
    if name == "openai":
        return OpenAIProvider()
    elif name == "claude":
        return ClaudeProvider()
    elif name == "gemini":
        return GeminiProvider()
    raise ValueError(f"Unknown provider: {name}")
