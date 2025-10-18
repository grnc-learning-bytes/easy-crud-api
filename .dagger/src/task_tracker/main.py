from typing import Annotated

import dagger
from dagger import DefaultPath, Doc, function, object_type


@object_type
class TaskTracker:
    @function
    async def test(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> str:
        """Return the result of running unit tests"""
        return await (
            self.build_env(source)
            .with_exec(["uv", "run", "ruff", "check"])
            .with_exec(["uv", "run", "ruff", "format", "--check"])
            .with_exec(["uv", "run", "mypy", "."])
            .with_exec(["uv", "run", "pytest", "tests/backend/unit", "-v"])
            .stdout()
        )

    @function
    def build_env(
        self,
        source: Annotated[
            dagger.Directory, DefaultPath("/"), Doc("task-tracker source directory")
        ],
    ) -> dagger.Container:
        """Build a ready-to-use development environment"""
        return source.docker_build()
