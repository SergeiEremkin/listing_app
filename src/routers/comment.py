from fastapi import APIRouter, Depends
from src.dependencies import get_db
from src.entities.web.comment import CreateComment
from src.services.comment import create_comment_service


router = APIRouter(
    prefix="/comment",
    tags=["comment"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})


@router.post('/')
async def create_comment(listing_id: int, user_id: int, comment_web: CreateComment, db=Depends(get_db)):
    return await create_comment_service(db, comment_web, listing_id, user_id)
