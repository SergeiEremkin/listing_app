from src.entities.web.photo import CreatePhoto
from src.repositories.postgres.pg_tables import Photo


async def photo_to_db(web_photo: CreatePhoto) -> Photo:
    return Photo(photo_link=web_photo.photo_link, listing_id=web_photo.listing_id)
