
import pytest

@pytest.fixture
def valid_user():
    return {"username": "testuser", "password": "password123"}

@pytest.fixture
def invalid_user():
    return {"username": "wronguser", "password": "wrongpassword"}