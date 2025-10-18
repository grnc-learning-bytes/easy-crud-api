from typing import Annotated

import dagger
from dagger import dag, DefaultPath, Doc, function, object_type

############
# Commands #
############

lint_tests_command: list[str] = ["uv", "run", "ruff", "check"]
fmt_tests_command: list[str] = ["uv", "run", "ruff", "format", "--check"]
type_tests_command: list[str] = ["uv", "run", "mypy", "."]
unit_tests_command: list[str] = ["uv", "run", "pytest", "tests/backend/unit", "-v"]

######################
# Pipeline functions #
######################


@object_type
class TaskTracker:
    #########
    # Tests #
    #########

    @function
    async def test_local(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> str:
        """Runs a collection of local tests"""
        return await (
            self.build_env(source)
            .with_exec(fmt_tests_command)
            .with_exec(lint_tests_command)
            .with_exec(type_tests_command)
            .with_exec(unit_tests_command)
            .stdout()
        )

    @function
    async def test_fmt(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> str:
        """Runs formatting tests"""
        return await self.build_env(source).with_exec(fmt_tests_command).stdout()

    @function
    async def test_lint(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> str:
        """Runs Linting tests"""
        return await self.build_env(source).with_exec(lint_tests_command).stdout()

    @function
    async def test_types(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> str:
        """Runs type tests"""
        return await self.build_env(source).with_exec(type_tests_command).stdout()

    @function
    async def test_unit(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> str:
        """Runs unit tests"""
        return await self.build_env(source).with_exec(unit_tests_command).stdout()

    ############
    # Building #
    ############

    @function
    def build_env(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> dagger.Container:
        """Build a ready-to-use development environment"""
        uv_image = dag.container().from_("ghcr.io/astral-sh/uv:0.9")
        return (
            dag.container()
            .from_("python:3.13-slim")
            .with_file("/bin/uv", uv_image.file("/uv"))
            .with_file("/bin/uvx", uv_image.file("/uvx"))
            .with_directory("/app", source)
            .with_workdir("/app")
            .with_exec(["uv", "sync", "--no-dev", "--locked"])
        )
