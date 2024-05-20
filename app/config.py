import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRES_MINUTES: int

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')

    @property
    def DATABASE_URL(self):
        return f'postgresql+psycopg2://postgres:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/postgres'


settings = Settings()
