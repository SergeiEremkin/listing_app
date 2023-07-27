from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.category import Category


async def add_category(session: AsyncSession, db_category: Category):
    session.add(db_category)
    await session.commit()
