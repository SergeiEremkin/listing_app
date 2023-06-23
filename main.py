from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src.services import crud
from src.entities.db import user_db, listing_db
from src.entities.web import listing_web, user_web
from src.repositories.postgres.database import SessionLocal, engine
from src.mappers import parse_frogs
user_db.Base.metadata.create_all(bind=engine)
listing_db.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def show_frogs():
    img_urls = parse_frogs('http://allaboutfrogs.org/funstuff/randomfrog.html')
    return img_urls


@app.post("/users/", response_model=user_web.User)
async def create_user(user_validation: user_web.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user_validation.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user_validation=user_validation)


@app.get("/users/", response_model=list[user_web.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=user_web.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=listing_web.Listing)
async def create_item_for_user(
        user_id: int, listing: listing_web.ListingCreate, db: Session = Depends(get_db)
):
    return crud.create_user_listing(db=db, listing_validation=listing, user_id=user_id)


@app.get("/items/", response_model=list[listing_web.Listing])
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_listings(db, skip=skip, limit=limit)
    return items
