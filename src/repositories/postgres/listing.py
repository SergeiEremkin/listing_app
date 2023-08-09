from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.listing import Listing


async def add_listing(session: AsyncSession, db_listing: Listing):
    session.add(db_listing)
    await session.commit()


async def delete_listing(session: AsyncSession, db_listing: Listing):
    await session.delete(db_listing)
    await session.commit()
