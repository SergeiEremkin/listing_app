from pydantic import BaseModel


class CreatePhoto(BaseModel):
    photo_link: str

    class Config:
        orm_mode = True


class Photo(CreatePhoto):
    id: int
    listing_id: int
