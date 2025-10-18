# Task tracker

A simple project to explore Backend code design concepts.


## Database Model

![](./assets/db-model.svg)


## Tools

- **Testing**:
  - Type tests: `mypy`
  - Software tests: `pytest`
- **API**: `fastapi` + `uvicorn`
- **Dependency Injection**: `dependency-injector`
- **Database**: `sqlmodel`
- **Settings Management**: `pydantic-settings`
- **Linting and formatting**: `ruff`
- **CICD**: GitHub Actions and `dagger`
- **Dependency Management**: `uv`

## Development

### Setup environment

Run `uv sync`

### Run tests

- Linting: `uv run ruff check` (run `uv run ruff check --fix` for auto-fixes)
- Formatting: `uv run ruff format --check` (run `uv run ruff format` to auto-format)
- Type tests: `uv run mypy .`
- Unit tests: `uv run pytest tests/backend/unit -v`
