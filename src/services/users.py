import asyncio

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from src.dependencies import get_db
from src.repositories.postgres.pg_tables.user import User
from src.entities.web import user
from src.repositories.postgres.users import add_user


async def get_user_by_id_service(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).where(User.id == user_id).options(selectinload(User.listings)))
    return result.scalar()


#
#
# async def get_user_by_email(db: Session, email: str):
#     return db.query(user.User).filter(user.User.email == email).first()


async def get_users_service(session: AsyncSession, skip: int = 0, limit: int = 100):
    result = await session.execute(
        select(User).order_by(User.name.desc()).offset(skip).limit(limit).options(selectinload(User.listings)))
    return result.scalars().all()


async def create_user_service(session: AsyncSession, user_validation: user.CreateUser) -> User:
    db_user = User(name=user_validation.name, email=user_validation.email,
                   hashed_password=user_validation.hashed_password)
    await add_user(session, db_user)
    return db_user
