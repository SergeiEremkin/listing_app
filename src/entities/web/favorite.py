from pydantic import BaseModel


class CreateFavorite(BaseModel):
    user_id: int
    listing_id: int

    class Config:
        orm_mode = True


class Favorite(CreateFavorite):
    id: int
