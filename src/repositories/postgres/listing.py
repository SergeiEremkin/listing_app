from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.postgres.pg_tables.listing import Listing
from src.entities.web.listing import CreateListing


async def add_listing(session: AsyncSession, db_listing: CreateListing):
    session.add(db_listing)
    await session.commit()
