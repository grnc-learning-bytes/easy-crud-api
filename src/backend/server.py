from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Literal

from src.backend.routers import (
    users,
    tasks,
)

app = FastAPI()
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")

@app.get("/health")
def health() -> Literal["healthy"]:
    return "healthy"
