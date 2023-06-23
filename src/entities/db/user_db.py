from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.repositories.postgres.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, default=None, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    listings = relationship("Listing", back_populates="user")
