from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.repositories.postgres.database import Base
from src.repositories.postgres.pg_tables.category import Category

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True)
    url = Column(String, nullable=False, unique=False)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey(Category.id))
    user = relationship("User", back_populates="listings", lazy='select')
    category = relationship("Category", back_populates="listings", lazy="select")