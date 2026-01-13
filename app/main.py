from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from app.api.generate import router

app = FastAPI(title="AI Model Router")

app.include_router(router)
