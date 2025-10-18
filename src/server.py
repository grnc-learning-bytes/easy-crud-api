from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.routers import (
    users,
    tags,
    tasks,
)

app = FastAPI()
app.include_router(users.router)
app.include_router(tags.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}
