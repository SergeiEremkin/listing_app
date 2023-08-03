from pydantic import BaseModel
from src.entities.web.listing import Listing


class CreateUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class User(CreateUser):
    id: int
    listing: list[Listing]
