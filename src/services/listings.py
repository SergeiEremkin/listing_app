from datetime import datetime
from fastapi import HTTPException
from sqlalchemy import select
from src.mappers.listing_mapper import listing_to_db, listing_to_web
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.photo import add_photo
from src.repositories.postgres.rank import add_rank
from src.repositories.postgres.listing import add_listing, delete_listing
from src.repositories.postgres.pg_tables.listing import Listing
from src.repositories.postgres.pg_tables.rank import Rank
from src.entities.web import listing
from random import randint, choice

from src.services.photos import auto_create_photo
from src.settings import Settings


settings = Settings()


async def get_listings_service(session: AsyncSession, skip: int = 0, limit: int = 100) -> list[listing.Listing]:
    db_listings = await session.execute(select(Listing).offset(skip).limit(limit))
    return [await listing_to_web(db_listing) for db_listing in db_listings.scalars().all()]


async def create_user_listing_service(session: AsyncSession, web_listing: listing.CreateListing,
                                      user_id: int, rank_id: int) -> Listing:
    db_listing = await listing_to_db(web_listing, user_id=user_id, rank_id=rank_id)
    await add_listing(session, db_listing)
    return db_listing


async def delete_user_listing_service(session: AsyncSession,
                                      user_id: int, listing_id: int) -> dict[str, bool]:
    db_listing = await session.execute(
        select(Listing).where(Listing.user_id == user_id).where(Listing.id == listing_id))
    if not db_listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    await delete_listing(session, db_listing.scalar())
    return {"ok": True}


async def get_listing_by_user_id_service(session: AsyncSession, user_id: int) -> listing.Listing:
    db_listings = await session.execute(select(Listing).where(Listing.user_id == user_id))
    return await listing_to_web(db_listings.scalar())


async def auto_create_listings(session: AsyncSession) -> dict[str: True]:
    await add_rank(session, Rank(category="Недвижимость", subcategory="Новое"))
    await add_rank(session, Rank(category="Личные вещи", subcategory="Б/у"))
    ranks_id = await session.execute(select(Rank.id))
    ranks_id = ranks_id.scalars().all()
    for i in range(1, 11):
        random_user_id = randint(1, 10)
        await add_listing(session, Listing(title=f"title{i}", created_at=datetime.now(), description=f"description{i}", price=i * 1000,
                                           rank_id=choice(ranks_id),
                                           user_id=random_user_id))
    listings_id = await session.execute(select(Listing.id))
    listings_id = listings_id.scalars().all()
    await auto_create_photo(session, choice(listings_id))
    await auto_create_photo(session, choice(listings_id))
    await auto_create_photo(session, choice(listings_id))
    return {"ok": True}
