from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    miniouri:str
    miniokey:str
    miniobucket:str
    miniosecret:str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")



@lru_cache(maxsize=20)
def get_settings():
    return Settings()