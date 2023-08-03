from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class User(CreateUser):
    id: int
