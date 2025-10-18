from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings


class PgSettings(BaseSettings):
    dsn: PostgresDsn = Field(validation_alias="DATABASE_DSN")

