import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_user_registration(client):
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = client.post('/api/signup', json=data)
    assert response.status_code == 201

def test_user_login(client):
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = client.post('/api/login', json=data)
    assert response.status_code == 200
    assert 'access_token' in response.json

# Add more test cases as needed

