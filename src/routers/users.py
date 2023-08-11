from fastapi import APIRouter, Depends
from src.dependencies import get_db
from src.entities.web.user import CreateUser
from src.services.users import create_user_service, auto_create_user_service, delete_user_service, update_user_service,\
    get_user_by_id_service, get_users_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}}
)


@router.get("/{user_id}")
async def get_user_by_id(user_id: int, db=Depends(get_db)):
    return await get_user_by_id_service(db, user_id)


@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db=Depends(get_db), ):
    return await get_users_service(db, skip=skip, limit=limit)


@router.post("/auto_create")
async def auto_create_user(db=Depends(get_db)):
    return await auto_create_user_service(db)


@router.post("/create")
async def create_user(user_db: CreateUser, db=Depends(get_db)):
    return await create_user_service(db, user_db)


@router.post("/delete/{user_id}")
async def delete_user_account(user_id: int, db=Depends(get_db)):
    return await delete_user_service(db, user_id)


@router.post("/update/{user_id}")
async def update_user(user_id: int, db=Depends(get_db)):
    return await update_user_service(db, user_id)


