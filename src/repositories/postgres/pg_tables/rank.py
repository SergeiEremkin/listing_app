from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.repositories.postgres.database import Base


class Rank(Base):
    __tablename__ = "ranks"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    category = Column(String)
    subcategory = Column(String)
    listing = relationship("Listing", back_populates='rank', lazy="select")


