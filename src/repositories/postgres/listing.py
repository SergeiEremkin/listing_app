from sqlalchemy.ext.asyncio import AsyncSession

from src.entities.web.listing import Listing


async def add_listing(session: AsyncSession, db_listing: Listing):
    session.add(db_listing)
    await session.commit()
    await session.refresh(db_listing)


