from pydantic import BaseModel


class ListingBase(BaseModel):
    title: str
    description: str | None = None


class ListingCreate(ListingBase):
    pass


class Listing(ListingBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool


class UserCreate(UserBase):
    pass


class User(BaseModel):
    id: int
    name: str
    email: str
    hashed_password: str
    is_active: bool
    listings: list[Listing] = []

    class Config:
        orm_mode = True
