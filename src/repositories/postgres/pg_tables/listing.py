
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from src.repositories.postgres.database import Base



class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    rank_id = Column(Integer, ForeignKey("ranks.id"))
    photo_id = Column(Integer, ForeignKey("photos.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="listings", lazy='select')
    rank = relationship("Rank", back_populates="listings", lazy="select")
    photo = relationship("Photo", back_populates="listings", lazy="select")
