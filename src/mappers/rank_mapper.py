from src.entities.web.rank import CreateRank
from src.repositories.postgres.pg_tables import Rank


async def rank_to_db(web_rank: CreateRank) -> Rank:
    return Rank(categories=web_rank.categories, subcategories=web_rank.subcategories)