import enum

from pydantic import BaseModel


class CreateListing(BaseModel):
    title: str
    description: str | None = None

    class Config:
        orm_mode = True


class Listing(CreateListing):
    category_id: int
    id: int
    user_id: int
    url: str
