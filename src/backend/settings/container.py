from dependency_injector.containers import DynamicContainer
from dependency_injector.providers import Singleton

from src.backend.repositories.tasks.in_memory import InMemoryTaskRepo
from src.backend.services.tasks import TaskService


class DepsContainer(DynamicContainer):
    def build(self) -> None:
        self.task_repo = Singleton(InMemoryTaskRepo)
        self.task_service = Singleton(TaskService, task_repo=self.task_repo())


class Container:
    _container: DepsContainer | None = None

    @classmethod
    def container(cls) -> DepsContainer:
        if cls._container is None:
            cls._container = DepsContainer()
            cls._container.build()
        return cls._container
