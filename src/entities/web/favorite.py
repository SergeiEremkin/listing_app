from pydantic import BaseModel


class CreateFavorite(BaseModel):
    pass

    class Config:
        orm_mode = True


class Favorite(CreateFavorite):
    id: int
    user_id: int
    listing_id: int