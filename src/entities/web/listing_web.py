from pydantic import BaseModel


class ListingBase(BaseModel):
    title: str
    description: str | None = None



class ListingCreate(ListingBase):
    pass


class Listing(ListingBase):
    id: int
    user_id: int
    url: str

    class Config:
        orm_mode = True
