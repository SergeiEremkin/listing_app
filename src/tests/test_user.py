import pytest


async def test_create_user_success(async_client):
    request_data = {
        "name": "test_name",
        "email": "test_email",
        "hashed_password": "test_password",
    }
    response = (await async_client.post(
        "/users/",
        json=request_data

    ))
    assert response.status_code == 200
    response = response.json()
    assert response["id"] is not None
    assert response["name"] == "test_name"
    assert response["email"] == "test_email"
    assert response["hashed_password"] == "test_password"


async def test_existing_user(async_client, user):
    user_db = user
    response = await async_client.get(f"/users/{user_db.id}")
    assert response.status_code == 200
    user = response.json()
    assert user["name"] == user_db.name
    assert user["id"] == user_db.id


async def test_create_user_listing_success(async_client, user):
    user_db = user
    request_data = {
        "title": "test_title",
        "description": "test_description"
    }
    response = await async_client.post(f"listings/{user_db.id}/listing/", json=request_data)
    assert response.status_code == 200
    listing = response.json()
    assert listing["title"] == "test_title"
    assert listing["description"] == "test_description"
    assert listing["user_id"] == user_db.id


# async def test_existing_listings(async_client, listings):
#     response = await async_client.get("/listings/")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["total_count"] == len(listings)
#     assert len(data["listings"]) == len(listings)
#     print(listings)
#     for i, listing in enumerate(data["listings"]):
#         assert listing["title"] == listings[i].title
#         assert listing["description"] == listings[i].description
#         assert listing["user_id"] == listings[i].user_id
#         assert listing["id"] == listings[i].id


if __name__ == '__main__':
    pytest.main(['-v'])
