import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import text, NullPool
from sqlalchemy.orm import sessionmaker

from src.dependencies import get_db
from main import app
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.entities.web.user import CreateUser
from src.repositories.postgres.database import Base
from src.repositories.postgres.pg_tables.user import User
from src.services.users import create_user_service
from src.settings import Settings

settings = Settings()

TEST_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://" \
                               f"{settings.test_db_username}:" \
                               f"{settings.test_db_password}@" \
                               f"{settings.db_host}:" \
                               f"{settings.db_port}/" \
                               f"{settings.test_db_database}"

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://" \
                          f"{settings.db_username}:" \
                          f"{settings.db_password}@" \
                          f"{settings.db_host}:" \
                          f"{settings.db_port}/" \
                          f"{settings.db_database}"


@pytest.fixture(scope="session")
def event_loop() -> asyncio.AbstractEventLoop:
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def engine():
    engine = create_async_engine(TEST_SQLALCHEMY_DATABASE_URL)
    yield engine
    engine.sync_engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def prepare_db():
    create_db_engine = create_async_engine(
        TEST_SQLALCHEMY_DATABASE_URL,
        isolation_level="AUTOCOMMIT",
    )
    async with create_db_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        # await connection.execute(text(
        #     f"DROP DATABASE IF EXISTS {settings.test_db_database};"
        #
        # )
        #
        # )
        # await connection.execute(
        #     text(f"CREATE DATABASE {settings.test_db_database};")
        # )


@pytest_asyncio.fixture(scope="session")
async def db_session(engine) -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        TestingSessionLocal = sessionmaker(
            expire_on_commit=False,
            class_=AsyncSession,
            bind=engine,
        )
        async with TestingSessionLocal(bind=connection) as session:
            yield session
            # await session.flush()
            # await session.rollback()


@pytest.fixture(scope="session")
def override_get_db(prepare_db, db_session: AsyncSession):
    async def _override_get_db():
        yield db_session

    return _override_get_db


@pytest_asyncio.fixture(scope="session")
async def async_client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture
async def user(db_session: AsyncSession) -> User:
    user = CreateUser(email="nanny_ogg@lancre.com", name="Gytha Ogg", hashed_password="12345678")
    user_db = await create_user_service(db_session, user)
    yield user_db
    await db_session.delete(user_db)
    await db_session.commit()
