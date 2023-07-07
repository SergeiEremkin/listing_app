from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.postgres.pg_tables.user import User


async def add_user(session: AsyncSession, db_user: User):
    session.add(db_user)
    await session.commit()

