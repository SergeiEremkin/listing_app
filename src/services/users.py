from src.mappers.user_mapper import users_from_orm_obj_to_pydentic_list, user_from_orm_obj_to_pydentic_list, \
    user_by_email_from_orm_obj_to_pydentic_list
from src.mappers.user_mapper import user_from_pydentic_to_orm_obj
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
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
    db_user = await user_from_pydentic_to_orm_obj(user_validation)
    await add_user(session, db_user)
    return db_user
