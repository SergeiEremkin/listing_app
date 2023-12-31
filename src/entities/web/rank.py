from enum import Enum
from pydantic import BaseModel


class RankEnum(str, Enum):
    real_estate = 'Недвижимость'
    auto = 'Автомобили'
    personal_items = 'Личные вещи'


class StateEnum(str, Enum):
    past_in_usage = 'Б/у'
    new = 'Новое'


class CreateRank(BaseModel):
    category: RankEnum
    subcategory: StateEnum


    class Config:
        orm_mode = True


class Rank(CreateRank):
    id: int
