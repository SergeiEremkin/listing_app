from src.entities.web.comment import CreateComment
from src.mappers.comment_mapper import comment_to_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.postgres.pg_tables.comment import Comment
from src.repositories.postgres.photo import add_photo


async def create_comment_service(session: AsyncSession, web_comment: CreateComment, listing_id: int,
                                 user_id: int) -> Comment:
    db_comment = await comment_to_db(web_comment, listing_id, user_id)
    await add_photo(session, db_comment)
    return db_comment
