from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from typing import Optional, Dict


class GenerateRequest(BaseModel):
    prompt: str
    model: Optional[str] = None
    parameters: Optional[Dict] = {}


class GenerateResponse(BaseModel):
    text: str
    model: str
    usage: Dict
