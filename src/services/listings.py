import asyncio
from random import randint
from typing import Any

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.postgres.listing import add_listing
from src.repositories.postgres.pg_tables.listing import Listing
from src.services.parser import image_parser, image_gen
from src.entities.web import listing
from src.settings import Settings

settings = Settings()


async def get_listings_service(session: AsyncSession, skip: int = 0, limit: int = 100):
    db_listings = await session.execute(select(Listing).offset(skip).limit(limit))
    return db_listings.scalars().all()


async def create_user_listing_service(session: AsyncSession, listing_validation: listing.CreateListing,
                                      user_id: int) -> Listing:
    images = await image_parser(settings.url_site)
    image = image_gen(images)
    db_listing = Listing(title=listing_validation.title,
                         description=listing_validation.description, url=await anext(image),
                         user_id=user_id)
    await add_listing(session, db_listing)
    return db_listing


async def create_random_user_listing_service(session: AsyncSession, user_id: int = 1) -> Listing:
    MIN_NUM = 0
    MAX_NUM = 100
    rnd_num = randint(MIN_NUM, MAX_NUM)
    images = await image_parser(settings.url_site)
    image = image_gen(images)
    db_listing = Listing(title=f'title{rnd_num}', description=f'description{rnd_num}',
                         url=await anext(image), user_id=user_id)
    await add_listing(session, db_listing)
    return db_listing