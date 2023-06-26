from fastapi import Depends, FastAPI

from src.entities.db import user_db, listing_db

from src.repositories.postgres.database import engine

from src.dependencies import get_db
from src.routers import users, listings

user_db.Base.metadata.create_all(bind=engine)
listing_db.Base.metadata.create_all(bind=engine)

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(users.router)
app.include_router(listings.router)
