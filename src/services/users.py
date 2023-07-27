from src.entities.web.listing import CreateListing
from src.entities.web.user import CreateUser
from src.mappers.listing_mapper import to_db_listing
from src.mappers.user_mapper import users_from_orm_obj_to_pydentic_list, user_from_orm_obj_to_pydentic_list, \
    user_by_email_from_orm_obj_to_pydentic_list
from src.mappers.user_mapper import to_db_user
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.repositories.postgres.listing import add_listing
from src.repositories.postgres.pg_tables.user import User
from src.entities.web import user
from src.repositories.postgres.users import add_user


async def get_user_by_id_service(session: AsyncSession, user_id: int) -> user.User:
    result = await session.execute(select(User).where(User.id == user_id).options(selectinload(User.listings)))
    return await user_from_orm_obj_to_pydentic_list(result.scalar())


async def get_user_by_email_service(session: AsyncSession, email: str):
    db_user = await session.execute(select(User).where(User.email == email).options(selectinload(User.listings)))
    return await user_by_email_from_orm_obj_to_pydentic_list(db_user.scalar(), email=email)


async def get_users_service(session: AsyncSession, skip: int = 0, limit: int = 100) -> list[user.User]:
    users_from_db = await session.execute(
        select(User).order_by(User.name.desc()).offset(skip).limit(limit).options(selectinload(User.listings)))
    return await users_from_orm_obj_to_pydentic_list(users_from_db.scalars().all())


async def create_user_service(session: AsyncSession, user_validation: user.CreateUser) -> User:
    db_user = await to_db_user(user_validation)
    await add_user(session, db_user)
    return db_user


async def auto_create_user_service(session: AsyncSession):


    listing_validation_1 = CreateListing(title="title_1", description="description_1")
    listing_validation_2 = CreateListing(title="title_2", description="description_2")
    listing_validation_3 = CreateListing(title="title_3", description="description_3")

    user_validation_1 = CreateUser(name="User_1", email="1@email.ru", hashed_password="password_1")
    user_validation_2 = CreateUser(name="User_2", email="2@email.ru", hashed_password="password_2")
    user_validation_3 = CreateUser(name="User_3", email="3@email.ru", hashed_password="password_3")

    db_user_1 = await to_db_user(user_validation_1)
    db_user_2 = await to_db_user(user_validation_2)
    db_user_3 = await to_db_user(user_validation_3)

    db_listing_1 = await to_db_listing(listing_validation_1, 1, 1)
    db_listing_2 = await to_db_listing(listing_validation_2, 2, 2)
    db_listing_3 = await to_db_listing(listing_validation_3, 3, 3)

    await add_user(session, db_user_1)
    await add_user(session, db_user_2)
    await add_user(session, db_user_3)

    await add_listing(session, db_listing_1)
    await add_listing(session, db_listing_2)
    await add_listing(session, db_listing_3)

    return user_validation_1, user_validation_2, user_validation_3
