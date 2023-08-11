from src.entities.web.photo import CreatePhoto
from src.repositories.postgres.pg_tables.photo import Photo


async def photo_to_db(web_photo: CreatePhoto, listing_id: int) -> Photo:
    return Photo(photo_link=web_photo.photo_link, listing_id=listing_id)
