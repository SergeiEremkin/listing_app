from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.favorite import Favorite


async def add_favorite(session: AsyncSession, db_favorite: Favorite):
    session.add(db_favorite)
    await session.commit()
