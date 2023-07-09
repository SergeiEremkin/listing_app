import asyncio
from random import randint
from typing import Any
from src.mappers.mappers import listings_from_orm_obj_to_pydentic_list
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.postgres.listing import add_listing
from src.repositories.postgres.pg_tables.listing import Listing
from src.services.parser import image_generator, random_number
from src.entities.web import listing
from src.settings import Settings

settings = Settings()


async def get_listings_service(session: AsyncSession, skip: int = 0, limit: int = 100) -> list[listing.Listing]:
    db_listings = await session.execute(select(Listing).offset(skip).limit(limit))
    return await listings_from_orm_obj_to_pydentic_list(db_listings.scalars().all())


async def create_user_listing_service(session: AsyncSession, listing_validation: listing.CreateListing,
                                      user_id: int) -> Listing:
    db_listing = Listing(title=listing_validation.title,
                         description=listing_validation.description, url=await anext(image_generator()),
                         user_id=user_id)
    await add_listing(session, db_listing)
    return db_listing


async def create_random_user_listing_service(session: AsyncSession, user_id: int = 1) -> Listing:
    db_listing = Listing(title=f'title{await random_number()}', description=f'description{await random_number()}',
                         url=await anext(image_generator()), user_id=user_id)
    await add_listing(session, db_listing)
    return db_listing
