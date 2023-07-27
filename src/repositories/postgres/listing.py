from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.listing import Listing


async def add_listing(session: AsyncSession, db_listing: Listing):
    session.add(db_listing)
    await session.commit()
