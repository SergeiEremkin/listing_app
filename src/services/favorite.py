from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.favorite import Favorite
from src.repositories.postgres.favorite import add_favorite


async def create_favorite_service(session: AsyncSession, listing_id: int,
                                  user_id: int) -> Favorite:
    favorite_db = Favorite(user_id=user_id, listing_id=listing_id)
    await add_favorite(session, favorite_db)
    return favorite_db
