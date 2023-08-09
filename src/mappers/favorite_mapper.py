from src.entities.web.favorite import CreateFavorite
from src.repositories.postgres.pg_tables import Favorite


async def favorite_to_db(listing_id: int, user_id: int) -> Favorite:
    return Favorite(user_id=user_id, listing_id=listing_id)
