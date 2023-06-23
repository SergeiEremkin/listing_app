from sqlalchemy.orm import Session

from src.entities.db import listing_db, user_db
from src.entities.web import listing_web, user_web


async def get_user(db: Session, user_id: int):
    return db.query(user_db.User).filter(user_db.User.id == user_id).first()


async def get_user_by_email(db: Session, email: str):
    return db.query(user_db.User).filter(user_db.User.email == email).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_db.User).offset(skip).limit(limit).all()


async def create_user(db: Session, user_validation: user_web.UserCreate):
    db_user = user_db.User(name=user_validation.name, email=user_validation.email,
                           hashed_password=user_validation.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_listings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(listing_db.Listing).offset(skip).limit(limit).all()


def create_user_listing(db: Session, listing_validation: listing_web.ListingCreate, user_id: int):
    db_listing = listing_db.Listing(**listing_validation.dict(), user_id=user_id)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing
