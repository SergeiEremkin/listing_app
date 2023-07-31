from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.repositories.postgres.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
