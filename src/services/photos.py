from src.entities.web.photo import CreatePhoto
from src.mappers.photo_mapper import photo_to_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables import photo
from src.repositories.postgres.photo import add_photo


async def create_photo_service(session: AsyncSession, web_photo: CreatePhoto, listing_id: int) -> photo.Photo:
    db_photo = await photo_to_db(web_photo, listing_id)
    await add_photo(session, db_photo)
    return db_photo
