from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from src.repositories.postgres.database import Base


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    photo_link = Column(String, nullable=False)
    listing_id = Column(String, ForeignKey("listings.id"), nullable=False)
    listing = relationship("Listing", back_populates="photo", lazy="select")


