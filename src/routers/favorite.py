from fastapi import APIRouter, Depends
from src.dependencies import get_db
from src.services.favorite import create_favorite_service


router = APIRouter(
    prefix="/favorite",
    tags=["favorite"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})


@router.post('/')
async def create_favorite(listing_id: int, user_id: int, db=Depends(get_db)):
    return await create_favorite_service(db, listing_id, user_id)
