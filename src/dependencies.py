from typing import AsyncGenerator

from src.repositories.postgres.database import SessionLocal


# Dependency
async def get_db() -> AsyncGenerator:
    async with SessionLocal() as session:
        yield session
