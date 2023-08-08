from pydantic import BaseModel, EmailStr
from src.entities.web.listing import Listing


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class User(CreateUser):
    id: int
    listing: list[Listing]
