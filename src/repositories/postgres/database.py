from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.settings import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://" \
                          f"{settings.db_username}:" \
                          f"{settings.db_password}@" \
                          f"{settings.db_host}:" \
                          f"{settings.db_port}/" \
                          f"{settings.db_database}"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


SessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
