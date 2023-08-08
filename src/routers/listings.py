from fastapi import APIRouter, Depends
from src.dependencies import get_db
from src.entities.web.listing import CreateListing
from src.entities.web.rank import CreateRank
from src.services.ranks import create_rank_service
from src.settings.settings import Settings
from src.services.listings import create_user_listing_service, get_listing_by_user_id_service, get_listings_service

settings = Settings()

router = APIRouter(
    prefix="/listings",
    tags=["listings"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})


@router.post("/{user_id}/{rank_id}")
async def create_listing_for_user(
        user_id: int, web_listing: CreateListing, web_rank: CreateRank, db=Depends(get_db)):
    rank_db = await create_rank_service(db, web_rank)
    return await create_user_listing_service(db, web_listing, user_id, rank_db.id)


@router.get("/{user_id}")
async def get_user_listings(user_id: int, db=Depends(get_db)):
    return await get_listing_by_user_id_service(db, user_id)


@router.get("/")
async def get_listings(db=Depends(get_db)):
    return await get_listings_service(db)
