import typer
import uvicorn

def main(
    app: str = "src.backend.server:app",
    host: str = "0.0.0.0",
    port: int = 5001,
    workers: int = 1,
    reload: bool = False,
) -> None:
    uvicorn.run(app=app, host=host, port=port, workers=workers, reload=reload)

typer.run(main)
