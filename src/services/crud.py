from fastapi import Depends

from src.dependencies import get_db

from sqlalchemy.orm import Session
from sqlalchemy import func
from src.entities.db import listing_db, user_db
from src.entities.web import listing_web, user_web
from src.mappers.parser import links_parser
from random import randint


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


async def get_listings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(listing_db.Listing).offset(skip).limit(limit).all()


async def create_user_listing(db: Session, listing_validation: listing_web.ListingCreate, user_id: int):
    p = links_parser('http://allaboutfrogs.org/funstuff/randomfrog.html')
    db_listing = listing_db.Listing(**listing_validation.dict(), url=next(p), user_id=user_id)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing


async def create_random_user_listing(db: Session, url: str, user_id: int = 1):
    MIN_NUM = 0
    MAX_NUM = 100
    rnd_num = randint(MIN_NUM, MAX_NUM)
    db_listing = listing_db.Listing(title=f'title{rnd_num}', description=f'description{rnd_num}',
                                    url=url, user_id=user_id)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing
