from src.entities.web.user import CreateUser
from src.repositories.postgres.users import User
from typing import Sequence, Any
from sqlalchemy import Row, RowMapping


# async def users_from_db_to_pydentic(orm_objects: Sequence[Row | RowMapping | Any]) -> list[user.User]:
#     users_list = []
#     for orm_object in orm_objects:
#         users_list.append(user.User(id=orm_object.id, name=orm_object.name, email=orm_object.email,
#                                     hashed_password=orm_object.hashed_password, is_active=orm_object.is_active,
#                                     listings=[orm_object.listing for orm_object.listing in orm_object.listings]))
#     return users_list


async def user_to_db(web_user: CreateUser) -> User:
    return User(name=web_user.name, email=web_user.email,
                password=web_user.password)

# async def user_by_email_from_orm_obj_to_pydentic_list(orm_object: Row | RowMapping | Any, email: str) -> user.User:
#     current_user = user.User(id=orm_object.id, name=orm_object.name, email=email,
#                              hashed_password=orm_object.hashed_password, is_active=orm_object.is_active,
#                              listings=[orm_object.listing for orm_object.listing in orm_object.listings])
#     return current_user
#
#
# async def to_db_user(user_validation: user.CreateUser) -> User:
#     return User(name=user_validation.name, email=user_validation.email,
#                 hashed_password=user_validation.hashed_password)
