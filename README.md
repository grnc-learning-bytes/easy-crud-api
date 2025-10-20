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
- **CICD**: GitHub Actions
- **Dependency Management**: `uv`

## Development

### Setup environment

Run `uv sync`

### Run tests

To run all local tests, run:

- `Formatting tests`: `uv run ruff format --check`
- `Linting tests`: `uv run ruff check`
- `Type tests`: `uv run mypy .`
- `Unit tests`: `uv run python -m pytest tests -vv`
