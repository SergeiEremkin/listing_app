from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import enum
from src.repositories.postgres.database import Base


# class Categories(enum.Enum):
#     real_estate = 'Недвижимость'
#     auto = 'Автомобили'
#     personal_items = 'Личные вещи'
#
#
# class State(enum.Enum):
#     past_in_usage = 'Б/у'
#     new = 'Новое'


class Rank(Base):
    __tablename__ = "ranks"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    category = Column(String)
    subcategory = Column(String)
    listing = relationship("Listing", back_populates='rank', lazy="select")


