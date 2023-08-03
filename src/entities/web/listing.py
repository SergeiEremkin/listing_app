import enum
from datetime import datetime
from pydantic import BaseModel


class CreateListing(BaseModel):
    user_id: int
    rank_id: int
    title: str
    description: str
    price: int

    class Config:
        orm_mode = True


class Listing(CreateListing):
    id: int
    created_at: datetime
