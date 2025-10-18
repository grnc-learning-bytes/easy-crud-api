# Task tracker

A simple project to explore Backend code design concepts.


## TODO

- [] GitHub actions
- [] User repository
  - [] Faker
  - [] Postgres
- [] User service
- [] User routes
- [] Tasks repository
  - [] Faker
  - [] Postgres
- [] Tasks service
- [] Tasks routes
- [] Authentication with JWT


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

We are using `dagger` to make local tests exactly the same as the ones run in CI.

To run all local tests, run: `dagger call test-local`. These include:

- `Formatting tests`: `dagger call test-fmt`
- `Linting tests`: `dagger call test-lint`
- `Type tests`: `dagger call test-types`
- `Unit tests`: `dagger call test-unit`
