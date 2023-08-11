from src.entities.web.user import CreateUser
from src.repositories.postgres.users import User
from src.entities.web import user
from typing import Any
from sqlalchemy import Row, RowMapping


async def user_to_web(user_db: Row | RowMapping | Any) -> user.User:
    return user.User(id=user_db.id,
                     name=user_db.name, email=user_db.email,
                     password=user_db.password,
                     listing=[listing for listing in user_db.listing])


async def user_to_db(web_user: CreateUser) -> User:
    return User(name=web_user.name, email=web_user.email,
                password=web_user.password)
