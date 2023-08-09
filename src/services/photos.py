from src.entities.web.photo import CreatePhoto
from src.mappers.photo_mapper import photo_to_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables import photo
from src.repositories.postgres.photo import add_photo
from src.services.parser import image_generator


async def create_photo_service(session: AsyncSession, web_photo: CreatePhoto, listing_id: int) -> photo.Photo:
    db_photo = await photo_to_db(web_photo, listing_id)
    await add_photo(session, db_photo)
    return db_photo


async def auto_create_photo(session: AsyncSession, listing_id: int):
    link = await anext(image_generator())
    await add_photo(session, photo.Photo(photo_link=link, listing_id=listing_id))
