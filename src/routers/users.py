from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from src.entities.web.user import User, CreateUser
from src.services.users import get_users_service, create_user_service, get_user_by_id_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=CreateUser)
async def create_user(user_validation: CreateUser, db=Depends(get_db)):
    return await create_user_service(db, user_validation)


@router.get("/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    return await get_users_service(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db=Depends(get_db)):
    db_user = await get_user_by_id_service(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
