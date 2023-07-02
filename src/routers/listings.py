import asyncio

from fastapi import APIRouter, Depends, Request
from src.dependencies import get_db
from src.entities.web.listing import Listing, CreateListing
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.settings.settings import Settings
from src.services.listings import create_user_listing_service, get_listings, create_random_user_listing

settings = Settings()

router = APIRouter(
    prefix="/listings",
    tags=["listings"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})

templates = Jinja2Templates(directory="src/templates")


@router.post("/{user_id}/random", response_model=CreateListing)
async def create_random_listing(user_id: int, db=Depends(get_db)):
    while True:
        await create_random_user_listing(db, user_id=user_id)
        await asyncio.sleep(10)


@router.post("/{user_id}/listing/", response_model=CreateListing)
async def create_listing_for_user(
        user_id: int, listing_validation: CreateListing, db=Depends(get_db)):
    return await create_user_listing_service(db, listing_validation, user_id)


@router.get("/", response_model=list[Listing], response_class=HTMLResponse)
async def read_listings(request: Request, skip: int = 0, limit: int = 100, db=Depends(get_db)):
    listings = await get_listings(db, skip=skip, limit=limit)
    return templates.TemplateResponse("listing.html", {"request": request, "listings": listings})
