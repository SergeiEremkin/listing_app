from src.entities.web.favorite import CreateFavorite
from src.repositories.postgres.pg_tables import Favorite


async def favorite_to_db(web_favorite: CreateFavorite) -> Favorite:
    return Favorite(user_id=web_favorite.user_id, listing_id=web_favorite.listing_id)
