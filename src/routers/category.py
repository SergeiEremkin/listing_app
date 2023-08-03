
from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from src.entities.web.rank import CreateRank
# from src.services.categories import create_category_service


# router = APIRouter(
#     prefix="/rank",
#     tags=["rank"],
#     dependencies=[Depends(get_db)],
#     responses={404: {"description": "Not found"}})
#
#
# @router.post('/')
# async def create_rank(rank: CreateRank, db=Depends(get_db)):
#     return await create_rank_service(db, rank)
