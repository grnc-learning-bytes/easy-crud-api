from dependency_injector.containers import DynamicContainer
from dependency_injector.providers import Singleton

from src.backend.repositories.users.interface import UserRepository
from src.backend.repositories.users.postgres import PgUserRepository
from src.backend.settings.settings import PgSettings


class Container(DynamicContainer):
    ######################################################
    # Build all the application dependencies dynamically #
    ######################################################

    def build(self):
        self.user_repo: Singleton[UserRepository] = Singleton(
            PgUserRepository, dsn=PgSettings()
        )
