from src.entities.web.rank import CreateRank
from src.repositories.postgres.pg_tables import Rank


async def rank_to_db(web_rank: CreateRank) -> Rank:
    return Rank(category=web_rank.category, subcategory=web_rank.subcategory)