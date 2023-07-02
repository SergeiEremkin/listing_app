import pytest
from fastapi.testclient import TestClient

from main import app
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.entities.web.user import CreateUser
from src.settings import Settings

test_client = TestClient(app)

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://" \
                          f"{settings.test_db_username}:" \
                          f"{settings.db_password}@" \
                          f"{settings.db_host}:" \
                          f"{settings.db_port}/" \
                          f"{settings.db_database}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

Base = declarative_base()


@pytest.fixture(scope="module")
async def init_models():
    async with engine.begin() as conn:

        try:
            yield conn.run_sync(Base.metadata.create_all)
        finally:
            await conn.run_sync(Base.metadata.drop_all)


SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


def test_create_user(init_models):
    user = CreateUser(
        name="Тест",
        email="Тест",
        hashed_password="Тест",
    )


if __name__ == '__main__':
    pytest.main()
