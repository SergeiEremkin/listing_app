from pydantic import BaseModel
from src.entities.web.listing_web import ListingBase, ListingCreate, Listing


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool
    listings: list[Listing] = []

    class Config:
        orm_mode = True
