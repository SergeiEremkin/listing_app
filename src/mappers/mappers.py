from typing import Sequence, Any

from sqlalchemy import Row, RowMapping

from src.entities.web import user
from src.entities.web import listing


async def users_from_orm_obj_to_pydentic_list(orm_objects: Sequence[Row | RowMapping | Any]) -> list[user.User]:
    users_list = []
    for orm_object in orm_objects:
        users_list.append(user.User(id=orm_object.id, name=orm_object.name, email=orm_object.email,
                                    hashed_password=orm_object.hashed_password, is_active=orm_object.is_active,
                                    listings=[orm_object.listing for orm_object.listing in orm_object.listings]))
    return users_list


async def user_from_orm_obj_to_pydentic_list(orm_object: Row | RowMapping | Any) -> user.User:
    current_user = user.User(id=orm_object.id, name=orm_object.name, email=orm_object.email,
                             hashed_password=orm_object.hashed_password, is_active=orm_object.is_active,
                             listings=[orm_object.listing for orm_object.listing in orm_object.listings])
    return current_user


async def listings_from_orm_obj_to_pydentic_list(orm_objects: Sequence[Row | RowMapping | Any]) -> \
        list[listing.Listing]:
    listings_list = []
    for orm_object in orm_objects:
        listings_list.append(
            listing.Listing(id=orm_object.id, title=orm_object.title, description=orm_object.description,
                            user_id=orm_object.user_id, url=orm_object.url))
    return listings_list
