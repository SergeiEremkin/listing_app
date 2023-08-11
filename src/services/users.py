from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.mappers.user_mapper import user_to_db, user_to_web
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.user import User
from src.entities.web import user
from src.repositories.postgres.users import add_user, delete_user


async def get_user_by_id_service(session: AsyncSession, user_id: int) -> user.User:
    user_db = await session.execute(select(User).where(User.id == user_id).options(selectinload(User.listing)))
    return await user_to_web(user_db.scalar())


async def get_users_service(session: AsyncSession, skip: int = 0, limit: int = 100) -> list[user.User]:
    users_list = []
    users_db = await session.execute(
        select(User).order_by(User.name.desc()).offset(skip).limit(limit).options(selectinload(User.listing)))
    for user_db in users_db.scalars().all():
        users_list.append(user_db)
    return users_list


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


async def update_user_service(session: AsyncSession, user_id: int):
    db_user = await session.execute(select(User).where(User.id == user_id))
    db_user.scalar().name = "Валера"
    await session.commit()
    return db_user


async def auto_create_user_service(session: AsyncSession):
    COUNT = 10
    for i in range(1, COUNT + 1):
        await add_user(session, User(name=f"User_{i}", email=f"{i}@email.ru", password=f"password_{i}"))
