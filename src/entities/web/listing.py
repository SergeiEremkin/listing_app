from datetime import datetime
from pydantic import BaseModel


class CreateListing(BaseModel):
    title: str
    description: str
    price: int

    class Config:
        orm_mode = True


class Listing(CreateListing):
    id: int
    user_id: int
    rank_id: int
    created_at: datetime
