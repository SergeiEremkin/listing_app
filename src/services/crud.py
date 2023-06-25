import random

from sqlalchemy.orm import Session

from src.entities.db import listing_db, user_db
from src.entities.web import listing_web, user_web
from src.mappers import parse_frogs


def get_user(db: Session, user_id: int):
    return db.query(user_db.User).filter(user_db.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user_db.User).filter(user_db.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_db.User).offset(skip).limit(limit).all()


def create_user(db: Session, user_validation: user_web.UserCreate):
    db_user = user_db.User(name=user_validation.name, email=user_validation.email,
                           hashed_password=user_validation.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_listings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(listing_db.Listing).offset(skip).limit(limit).all()


def create_user_listing(db: Session, listing_validation: listing_web.ListingCreate, user_id: int):
    frog_url = _generate_random_url()
    db_listing = listing_db.Listing(**listing_validation.dict(), url=frog_url, user_id=user_id)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing


def listing_random_generate(db: Session, user_id: int = 1):
    frog_url = _generate_random_url()
    rnd_num = _generate_random_number()
    db_listing = listing_db.Listing(title=f'title{rnd_num}', description=f'description{rnd_num}',
                                    url=frog_url, user_id=user_id)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing


def _generate_random_url() -> str:
    frogs_urls = parse_frogs('http://allaboutfrogs.org/funstuff/randomfrog.html')
    rnd_num = random.randint(0, len(frogs_urls))
    return frogs_urls[rnd_num]


def _generate_random_number() -> int:
    MIN = 0
    MAX = 100
    return random.randint(MIN, MAX)
