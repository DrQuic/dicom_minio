from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    miniouri:str
    miniokey:str
    miniobucket:str
    miniosecret:str
    postgresurl: str
    postgresuser: str
    postgrespassword: str
    postgresdb: str
    migratedb: bool
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = None


@lru_cache(maxsize=20)
def create_settings():
    print("Running  settings")
    global settings
    settings = Settings()


def get_settings():
    return settings