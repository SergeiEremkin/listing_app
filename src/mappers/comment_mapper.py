from src.entities.web.comment import CreateComment
from src.repositories.postgres.pg_tables import Comment


async def comment_to_db(web_comment: CreateComment, listing_id: int, user_id: int) -> Comment:
    return Comment(description=web_comment.description, listing_id=listing_id, user_id=user_id)
