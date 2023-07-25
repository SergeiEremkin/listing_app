from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum
from src.repositories.postgres.database import Base


class Categories(enum.Enum):
    real_estate = 'Недвижимость'
    auto = 'Автомобили'
    personal_items = 'Личные вещи'


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    categories = Column(Enum(Categories))
    listings = relationship("Listing", back_populates="category", lazy='select')

