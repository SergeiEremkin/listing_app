from unittest import mock

import pytest
from sqlalchemy import func, select


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


if __name__ == '__main__':
    pytest.main(['-v'])
