from datetime import datetime

from pydantic import BaseModel


class CreateComment(BaseModel):
    description: str


    class Config:
        orm_mode = True


class Comment(CreateComment):
    id: int
    created_at: datetime
