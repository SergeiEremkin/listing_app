# from typing import Sequence, Any
# from sqlalchemy import Row, RowMapping
#
from sqlalchemy import Row, RowMapping

from src.entities.web import listing
from src.repositories.postgres.pg_tables import Listing


#
# from src.repositories.postgres.pg_tables.listing import Listing
# from src.services.parser import image_generator, random_number
#
#
# async def listings_from_orm_obj_to_pydentic_list(orm_objects: Sequence[Row | RowMapping | Any]) -> \
#         list[listing.Listing]:
#     listings_list = []
#     for orm_object in orm_objects:
#         listings_list.append(
#             listing.Listing(id=orm_object.id, category_id=orm_object.category_id, title=orm_object.title, description=orm_object.description,
#                             user_id=orm_object.user_id, url=orm_object.url), )
#     return listings_list


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
