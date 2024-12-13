from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # APP
    APP_TITLE: str
    LOG_PATH: str

    # MongoDB
    MONGODB_USER: str
    MONGODB_AUTH_SOURCE: str
    MONGODB_PASS: str
    MONGODB_HOST: str
    MONGODB_PORT: int

    # CORS
    ORIGINS: list[str]

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'
