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

## Postgres

`docker run --name task-tracker -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres`

`export DATABASE_DSN=postgresql://postgres:postgres@localhost:5432/postgres`

`uv run alembic revision --autogenerate -m "Initial migration"`

`uv run alembic upgrade head`
