from pydantic import BaseSettings


class Settings(BaseSettings):
    db_username: str = 'postgres'
    db_password: str = 'postgres'
    db_database: str = 'postgres'
    db_host: str = 'localhost'
    db_port: int = 5432
    url_site: str = 'http://allaboutfrogs.org/funstuff/randomfrog.html'

    test_db_username: str = 'postgres_test'
    test_db_password: str = 'postgres_test'
    test_db_database: str = 'postgres-test'
    # test_db_host: str = 'localhost'
    # test_db_port: int = 5432

    class Config:
        env_file = ".env"
