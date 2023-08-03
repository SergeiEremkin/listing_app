from pydantic import BaseModel


class CreatePhoto(BaseModel):
    photo_link: str
    listing_id: int

    class Config:
        orm_mode = True


class Photo(CreatePhoto):
    id: int
