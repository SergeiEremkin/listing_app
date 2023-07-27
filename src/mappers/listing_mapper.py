from typing import Sequence, Any
from sqlalchemy import Row, RowMapping

from src.entities.web import listing

from src.repositories.postgres.pg_tables.listing import Listing
from src.services.parser import image_generator, random_number


async def listings_from_orm_obj_to_pydentic_list(orm_objects: Sequence[Row | RowMapping | Any]) -> \
        list[listing.Listing]:
    listings_list = []
    for orm_object in orm_objects:
        listings_list.append(
            listing.Listing(id=orm_object.id, category_id=orm_object.category_id, title=orm_object.title, description=orm_object.description,
                            user_id=orm_object.user_id, url=orm_object.url), )
    return listings_list


async def to_db_listing(listing_validation: listing.CreateListing, user_id: int = 1, category_id: int = 1) -> Listing:
    return Listing(title=listing_validation.title,
                   description=listing_validation.description, url=await anext(image_generator()),
                   user_id=user_id, category_id=category_id)


async def random_listing_from_pydentic_to_orm_obj(user_id: int = 1) -> Listing:
    return Listing(title=f'title{await random_number()}',
                   description=f'description{await random_number()}',
                   url=await anext(image_generator()), user_id=user_id)
