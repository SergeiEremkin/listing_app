import asyncio
from fastapi import APIRouter, Depends, Request
from src.dependencies import get_db
from src.entities.web.listing import CreateListing
from src.entities.web.rank import CreateRank
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.services.ranks import create_rank_service
from src.settings.settings import Settings
from src.services.listings import create_user_listing_service

settings = Settings()

router = APIRouter(
    prefix="/listings",
    tags=["listings"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})

templates = Jinja2Templates(directory="src/templates")


# @router.post("/{user_id}/random")
# async def create_random_listing(user_id: int, db=Depends(get_db)):
#     while True:
#         await create_random_user_listing_service(db, user_id=user_id)
#         await asyncio.sleep(10)


@router.post("/{user_id}/{rank_id}")
async def create_listing_for_user(
        user_id: int, web_listing: CreateListing, web_rank: CreateRank, db=Depends(get_db)):
    rank_db = await create_rank_service(db, web_rank)
    return await create_user_listing_service(db, web_listing, user_id, rank_db.id)

# @router.get("/", response_class=HTMLResponse)
# async def read_listings(request: Request, skip: int = 0, limit: int = 100, db=Depends(get_db)):
#     listings = await get_listings_service(db, skip=skip, limit=limit)
#     return templates.TemplateResponse("listing.html", {"request": request, "listings": listings})
