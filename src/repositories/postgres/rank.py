from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.rank import Rank


async def add_rank(session: AsyncSession, db_rank: Rank):
    session.add(db_rank)
    await session.commit()

