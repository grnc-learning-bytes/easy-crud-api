from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    dsn: PostgresDsn = Field(alias="DATABASE_DSN")
