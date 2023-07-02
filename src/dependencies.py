from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.postgres.database import SessionLocal


# Dependency
async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
