import yaml
import os



def load_router_config():
    path = os.getenv("ROUTER_CONFIG_PATH", "/app/app/config/config.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f)


# Example Config Structure
# default_model: gpt-4o
# models:
#   gpt-4o:
#     provider: openai
#   gemini-pro:
#     provider: gemini
