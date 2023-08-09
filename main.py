import uvicorn
from fastapi import Depends, FastAPI
from src.dependencies import get_db
from src.repositories.postgres.database import init_models
from src.routers import users, listings, photo, comment, favorite
from src.services.listings import auto_create_listings
from src.services.users import auto_create_user_service


app = FastAPI(dependencies=[Depends(get_db)])


@app.on_event("startup")
async def on_startup():
    await init_models()


@app.post("/")
async def create_base_objects(db=Depends(get_db)):
    await auto_create_user_service(db)
    await auto_create_listings(db)
    return {"user_create": True}


app.include_router(users.router)
app.include_router(listings.router)
app.include_router(photo.router)
app.include_router(comment.router)
app.include_router(favorite.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
