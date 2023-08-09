from fastapi import HTTPException
from sqlalchemy import select

from src.entities.web.listing import CreateListing
from src.entities.web.user import CreateUser
#from src.mappers.listing_mapper import to_db_listing

from src.mappers.user_mapper import user_to_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.repositories.postgres.listing import add_listing
from src.repositories.postgres.pg_tables.user import User
from src.entities.web import user
from src.repositories.postgres.users import add_user, delete_user


# async def get_user_by_id_service(session: AsyncSession, user_id: int) -> user.User:
#     result = await session.execute(select(User).where(User.id == user_id).options(selectinload(User.listings)))
#     return await user_from_orm_obj_to_pydentic_list(result.scalar())
#
#
# async def get_user_by_email_service(session: AsyncSession, email: str):
#     db_user = await session.execute(select(User).where(User.email == email).options(selectinload(User.listings)))
#     return await user_by_email_from_orm_obj_to_pydentic_list(db_user.scalar(), email=email)


# async def get_users_service(session: AsyncSession, skip: int = 0, limit: int = 100) -> list[user.User]:
#     users_from_db = await session.execute(
#         select(User).order_by(User.name.desc()).offset(skip).limit(limit).options(selectinload(User.listings)))
#     return await users_from_orm_obj_to_pydentic_list(users_from_db.scalars().all())


async def create_user_service(session: AsyncSession, web_user: user.CreateUser) -> User:
    db_user = await user_to_db(web_user)
    await add_user(session, db_user)
    return db_user


async def delete_user_service(session: AsyncSession, user_id: int) -> dict[str: bool]:
    db_user = await session.execute(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(session, db_user.scalar())
    return {"ok": True}


async def auto_create_user_service(session: AsyncSession):
    for i in range(1, 11):
        await add_user(session, User(name=f"User_{i}", email=f"{i}@email.ru", password=f"password_{i}"))
