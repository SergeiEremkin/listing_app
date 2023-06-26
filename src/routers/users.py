from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from src.entities.web import user_web, listing_web
from src.services import crud

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}}
)


@router.post("/", response_model=user_web.User)
async def create_user(user_validation: user_web.UserCreate, db=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_validation.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user_validation=user_validation)


@router.get("/", response_model=list[user_web.User])
async def read_users(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=user_web.User)
async def read_user(user_id: int, db=Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/count", response_model=user_web.User)
async def read_users_id(db=Depends(get_db)):
    count_users = crud.get_users_id(db=db)
    return {'count': count_users}
