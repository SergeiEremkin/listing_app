
from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from src.entities.web.category import CreateCategory
from src.services.categories import create_category_service


router = APIRouter(
    prefix="/category",
    tags=["category"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}})


@router.post('/')
async def create_category(category_validation: CreateCategory, db=Depends(get_db)):
    return await create_category_service(db, category_validation)
