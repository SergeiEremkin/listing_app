import asyncio

from fastapi import APIRouter, Depends, \
    Request
from src.dependencies import get_db
from src.entities.web import user_web, listing_web
from src.mappers.parser import links_parser
from src.services import crud
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/listings",
    tags=["listings"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})

templates = Jinja2Templates(directory="src/templates")


@router.post("/random", response_model=user_web.Listing)
async def create_random_listing(db=Depends(get_db), user_id: int = 1):
    p = links_parser('http://allaboutfrogs.org/funstuff/randomfrog.html')
    while True:
        url: str = next(p)
        await crud.create_random_user_listing(db=db, user_id=user_id, url=url)
        await asyncio.sleep(10)


@router.post("/{user_id}/items/", response_model=listing_web.Listing)
async def create_item_for_user(
        user_id: int, listing: listing_web.ListingCreate, db=Depends(get_db)
):
    return await crud.create_user_listing(db=db, listing_validation=listing, user_id=user_id)


@router.get("/", response_model=listing_web.Listing, response_class=HTMLResponse)
async def read_items(request: Request, skip: int = 0, limit: int = 100, db=Depends(get_db)):
    listings = await crud.get_listings(db, skip=skip, limit=limit)
    return templates.TemplateResponse("listing.html", {"request": request, "listings": listings})

