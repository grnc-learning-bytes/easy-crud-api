from fastapi.openapi.utils import get_openapi
import yaml

from src.backend.server import app

with open("openapi.yaml", "w") as f:
    yaml.safe_dump(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        f,
        indent=2,
    )
