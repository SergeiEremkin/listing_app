import uvicorn
from fastapi import Depends, FastAPI
from src.dependencies import get_db
from src.repositories.postgres.database import init_models
from src.routers import users, listings, photo, comment
app = FastAPI(dependencies=[Depends(get_db)])


@app.on_event("startup")
async def on_startup():
    await init_models()


app.include_router(users.router)
app.include_router(listings.router)
app.include_router(photo.router)
app.include_router(comment.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
