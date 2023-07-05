from fastapi.testclient import TestClient
from src.dependencies import get_db
from main import app
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.repositories.postgres.database import Base
from src.settings import Settings

settings = Settings()

test_app = TestClient(app)

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://" \
                          f"{settings.db_username}:" \
                          f"{settings.db_password}@" \
                          f"{settings.db_host}:" \
                          f"{settings.db_port}/" \
                          f"{settings.test_db_database}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

TestingSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_db] = override_get_db()

# @pytest.fixture(autouse=True)
# def create_dummy_user():
#     database = anext(override_get_db())
#     test_user = CreateUser(name='test', email='test',
#                            hashed_password='test')
#     database.add(test_user)
#     database.commit()
#
#     yield
#
#     database.query(User).filter(User.email == 'test').delete()
#     database.commit()


# if __name__ == '__main__':
#     pytest.main(['-v'])
