from unittest import mock

import pytest
from src.repositories.postgres.pg_tables.user import User


@pytest.mark.asyncio
async def test_create_user_success(async_client):
    request_data = {
        "name": "test_name",
        "email": "test_email",
        "hashed_password": "test_password",
    }
    response = await async_client.post(
        "/users/",
        json=request_data

    )
    assert response.status_code == 200
    assert response.json()["id"] is not None
    assert response.json()["name"] == "test_name"
    assert response.json()["email"] == "test_email"
    assert response.json()["hashed_password"] == "test_password"


@pytest.mark.asyncio
async def test_existing_user(async_client, user):
    user_db = user
    response = await async_client.get(f'/users/{user_db.id}')
    assert response.status_code == 200
    user = response.json()
    assert user["name"] == user_db.name
    assert user["id"] == user_db.id


if __name__ == '__main__':
    pytest.main(['-v'])
