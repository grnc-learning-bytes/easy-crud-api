from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Literal

from src.backend.routers import tasks


app = FastAPI(
    title="Task Tracker",
    description="An application for you to easily track your tasks!",
    version="0.0.1",
)
app.include_router(tasks.router)


@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@app.get("/health")
def health() -> Literal["healthy"]:
    return "healthy"
