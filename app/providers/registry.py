from .openai import OpenAIProvider


PROVIDERS = {
    "openai": OpenAIProvider(),
    # "gemini": GeminiProvider(),   # stub
    # "anthropic": AnthropicProvider()
}
