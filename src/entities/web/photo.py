from pydantic import BaseModel
from src.services.parser import image_generator


class CreatePhoto(BaseModel):
    photo_link: str

    class Config:
        orm_mode = True


class Photo(CreatePhoto):
    id: int
    listing_id: int
