from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from src.entities.web.user import CreateUser
from src.services.users import create_user_service, auto_create_user_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}}
)


@router.post("/create")
async def auto_create_user(db=Depends(get_db)):
    return await auto_create_user_service(db)


@router.post("/")
async def create_user(user_validation: CreateUser, db=Depends(get_db)):
    return await create_user_service(db, user_validation)


# @router.get("/")
# async def read_users(skip: int = 0, limit: int = 100, db=Depends(get_db)):
#     return await get_users_service(db, skip=skip, limit=limit)
#
#
# @router.get("/{user_id}")
# async def read_user(user_id: int, db=Depends(get_db)):
#     db_user = await get_user_by_id_service(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @router.get("/{email}")
# async def read_user_by_email(email: str, db=Depends(get_db)):
#     return await get_user_by_email_service(db, email=email)
