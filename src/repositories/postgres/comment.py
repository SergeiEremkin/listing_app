from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.comment import Comment


async def add_comment(session: AsyncSession, db_comment: Comment):
    session.add(db_comment)
    await session.commit()
