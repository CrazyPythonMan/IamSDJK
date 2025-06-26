from functools import lru_cache

from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL:str
    SECRET:str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def settings() -> Settings:
    return Settings()
if __name__ == '__main__':
    print(settings().DATABASE_URL)
