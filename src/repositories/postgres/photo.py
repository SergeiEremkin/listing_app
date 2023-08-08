from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.photo import Photo


async def add_photo(session: AsyncSession, db_photo: Photo):
    session.add(db_photo)
    await session.commit()
