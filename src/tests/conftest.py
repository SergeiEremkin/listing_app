import asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient
from src.dependencies import get_db
from main import app
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.entities.web.listing import CreateListing
from src.entities.web.user import CreateUser
from src.repositories.postgres.database import Base
from src.repositories.postgres.pg_tables import listing
from src.repositories.postgres.pg_tables import user
from src.services.listings import create_user_listing_service
from src.services.users import create_user_service
from src.settings import Settings

settings = Settings()

TEST_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://" \
                               f"{settings.DB_USERNAME}:" \
                               f"{settings.DB_PASSWORD}@" \
                               f"{settings.DB_HOST}:" \
                               f"{settings.DB_PORT}/" \
                               f"{settings.TEST_DB_DATABASE}"


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


@pytest_asyncio.fixture(scope="session")
async def db_session(engine) -> AsyncSession:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        TestingSessionLocal = async_sessionmaker(
            expire_on_commit=False,
            class_=AsyncSession,
            bind=engine,
        )
        async with TestingSessionLocal(bind=connection) as session:
            yield session


@pytest.fixture(scope="session")
def override_get_db(db_session: AsyncSession):
    async def _override_get_db():
        yield db_session

    return _override_get_db


@pytest_asyncio.fixture(scope="session")
async def async_client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture
async def user(db_session: AsyncSession) -> user.User:
    user = CreateUser(email="nanny_ogg@lancre.com", name="Gytha Ogg", password="12345678")
    user_db = await create_user_service(db_session, user)
    yield user_db
    await db_session.delete(user_db)
    await db_session.commit()


@pytest_asyncio.fixture()
async def listings(db_session: AsyncSession, user) -> list[listing.Listing]:
    listing_1 = CreateListing(title="test_title", description="description_test")
    listing_2 = CreateListing(title="test_title_2", description="description_test_2")
    listing_db_1 = await create_user_listing_service(db_session, listing_1, user_id=user.id)
    listing_db_2 = await create_user_listing_service(db_session, listing_2, user_id=user.id)
    yield [listing_db_1, listing_db_2]
    await db_session.delete(listing_db_1)
    await db_session.delete(listing_db_2)
    await db_session.commit()
