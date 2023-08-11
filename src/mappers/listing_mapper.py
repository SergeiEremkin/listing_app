# from typing import Sequence, Any
from sqlalchemy import Row, RowMapping
from src.entities.web import listing
from src.repositories.postgres.pg_tables.listing import Listing


async def listing_to_db(web_listing: listing.CreateListing, user_id: int, rank_id: int) -> Listing:
    return Listing(title=web_listing.title,
                   description=web_listing.description,
                   price=web_listing.price,
                   rank_id=rank_id,
                   user_id=user_id)


async def listing_to_web(listing_db: Row | RowMapping) -> listing.Listing:
    return listing.Listing(id=listing_db.id,
                           user_id=listing_db.user_id,
                           rank_id=listing_db.rank_id,
                           created_at=listing_db.created_at,
                           title=listing_db.title,
                           description=listing_db.description,
                           price=listing_db.price)
