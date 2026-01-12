from fastapi import APIRouter, HTTPException
from app.schemas import GenerateRequest, GenerateResponse
from app.config.loader import load_router_config
from app.providers.registry import get_provider

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    config = load_router_config()

    model = req.model or config["default_model"]
    model_cfg = config["models"].get(model)

    if not model_cfg:
        raise HTTPException(400, f"Unknown model: {model}")

    provider_name = model_cfg["provider"]
    provider = get_provider(provider_name)

    if not provider:
        raise HTTPException(500, f"Provider not enabled: {provider_name}")

    result = await provider.generate(
        prompt=req.prompt,
        model=model,
        parameters=req.parameters or {}
    )

    return result
