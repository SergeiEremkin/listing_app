from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import httpx
from main import app
from src.dependencies import get_db
from src.repositories.postgres.database import Base
from src.settings.settings import Settings

settings = Settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.db_username}:" \
                          f"{settings.db_password}" \
                          f"@{settings.db_host}:" \
                          f"{settings.db_port}/" \
                          f"{settings.db_database}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Игорь", "email": "2333@mail.ru", "hashed_password": "my_pass"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "2333@mail.ru"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "2333@mail.ru"
    assert data["id"] == user_id


if __name__ == '__main__':
    test_create_user()
    # print(DB_USERNAME)
    # print(DB_PORT)
