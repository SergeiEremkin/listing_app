from src.entities.web.comment import CreateComment
from src.repositories.postgres.pg_tables import Comment


async def comment_to_db(web_comment: CreateComment) -> Comment:
    return Comment(description=web_comment.description, listing_id=web_comment.listing_id, user_id=web_comment.user_id)
