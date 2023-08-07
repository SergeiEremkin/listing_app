from src.mappers.listing_mapper import listing_to_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.listing import add_listing
from src.repositories.postgres.pg_tables.listing import Listing
from src.entities.web import listing
from src.settings import Settings

settings = Settings()


#
#
# async def get_listings_service(session: AsyncSession, skip: int = 0, limit: int = 100) -> list[listing.Listing]:
#     db_listings = await session.execute(select(Listing).offset(skip).limit(limit))
#     return await listings_from_orm_obj_to_pydentic_list(db_listings.scalars().all())
#
#
async def create_user_listing_service(session: AsyncSession, web_listing: listing.CreateListing,
                                      user_id: int, rank_id: int) -> Listing:
    db_listing = await listing_to_db(web_listing, user_id=user_id, rank_id=rank_id)
    await add_listing(session, db_listing)
    return db_listing
#
#
# async def create_random_user_listing_service(session: AsyncSession, user_id: int = 1) -> Listing:
#     db_listing = await random_listing_from_pydentic_to_orm_obj(user_id=user_id)
#     await add_listing(session, db_listing)
#     return db_listing
