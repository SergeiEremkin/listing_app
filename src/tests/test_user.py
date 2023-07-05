import asyncio
import pytest
from httpx import AsyncClient
from src.entities.web.user import CreateUser
from src.services.users import create_user_service
from src.tests.conftest_db import override_get_db, init_models, test_app


# @pytest.mark.asyncio
# async def test_all_users():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.post("/users/", json={"name": "test", "email": "test",
#                                                   "hashed_password": "test"})
#     assert response.status_code == 201
#     assert response.json()["name"] == "test"


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        await init_models()
        db = await asyncio.create_task(override_get_db())
        new_user = CreateUser(name="test", email="test_email", hashed_password="testpassword")
        db_user = await create_user_service(await anext(db), new_user)
        response = await ac.get("/users")
    assert db_user.name == "test"
    assert response.status_code == 200


if __name__ == '__main__':
    pytest.main(['-v'])
