from app.providers.openai import OpenAIProvider

def get_provider(name: str):
    if name == "openai":
        return OpenAIProvider()
    raise ValueError(f"Unknown provider: {name}")
