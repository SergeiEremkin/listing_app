from fastapi import Depends, FastAPI
from src.repositories.postgres.database import init_models
from src.dependencies import get_db
from src.routers import users, listings

app = FastAPI(dependencies=[Depends(get_db)])



# @app.on_event("startup")
# async def on_startup():
#     await init_models()


app.include_router(users.router)
app.include_router(listings.router)
