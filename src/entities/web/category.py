from enum import Enum
from pydantic import BaseModel



class CategoriesEnum(str, Enum):
    real_estate = 'Недвижимость'
    auto = 'Автомобили'
    personal_items = 'Личные вещи'


class StateEnum(str, Enum):
    past_in_usage = 'Б/у'
    new = 'Новое'


class CreateCategory(BaseModel):
    categories: CategoriesEnum
    subcategories: StateEnum

    class Config:
        orm_mode = True


class Category(CreateCategory):
    id: int
