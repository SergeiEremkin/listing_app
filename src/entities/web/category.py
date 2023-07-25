import enum

from pydantic import BaseModel


class CreateCategory(BaseModel):
    categories: enum

    class Config:
        orm_mode = True


class Category(CreateCategory):
    id: int
