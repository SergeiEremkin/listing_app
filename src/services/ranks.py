from src.entities.web.rank import CreateRank
from src.mappers.rank_mapper import rank_to_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables import rank
from src.repositories.postgres.rank import add_rank


async def create_rank_service(session: AsyncSession, web_rank: CreateRank) -> rank.Rank:
    db_rank = await rank_to_db(web_rank)
    await add_rank(session, db_rank)
    return db_rank
