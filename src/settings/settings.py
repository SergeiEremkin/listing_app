from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str = 'postgres'
    DB_PASSWORD: str = 'postgres'
    DB_DATABASE: str = 'postgres'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    TEST_DB_DATABASE: str = 'postgres-test'
    url_site: str = 'http://allaboutfrogs.org/funstuff/randomfrog.html'

    class Config:
        env_file = ".env"
