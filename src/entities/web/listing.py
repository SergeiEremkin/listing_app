from pydantic import BaseModel


class CreateListing(BaseModel):
    title: str
    description: str | None = None

    class Config:
        orm_mode = True


class Listing(CreateListing):
    id: int
    user_id: int
    url: str
