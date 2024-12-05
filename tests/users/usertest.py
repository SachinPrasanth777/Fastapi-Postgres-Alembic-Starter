from fastapi.testclient import TestClient
from app import app
from faker import Faker

fake = Faker()
client = TestClient(app)


def get_user_data():
    user_data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": "password1",
    }

    response = client.post("/user/signup/", json=user_data)

    return user_data


def test_signup():
    signup_data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": "password1",
    }

    response = client.post("/user/signup/", json=signup_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User has been created"}


def test_login():
    login_data = get_user_data()
    response = client.post("/user/login/", json=login_data)

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
