from fastapi import APIRouter, Depends
from src.dependencies import get_db
from src.entities.web.photo import CreatePhoto
from src.services.photos import create_photo_service

router = APIRouter(
    prefix="/photo",
    tags=["photo"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})


@router.post('/')
async def create_photo(listing_id: int, photo_web: CreatePhoto, db=Depends(get_db)):
    return await create_photo_service(db, photo_web, listing_id)
