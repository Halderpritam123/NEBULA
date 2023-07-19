import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_get_all_users(client):
    response = client.get('/api/admin/users')
    assert response.status_code == 200

def test_get_all_properties(client):
    response = client.get('/api/admin/properties')
    assert response.status_code == 200

def test_get_all_bookings(client):
    response = client.get('/api/admin/bookings')
    assert response.status_code == 200

def test_update_user(client):
    # Replace 'user_id' with the ID of the user you want to update
    user_id = 'user_id'
    data = {
        'username': 'new_username'
    }
    response = client.put(f'/api/admin/user/{user_id}', json=data)
    assert response.status_code == 200

def test_delete_user(client):
    # Replace 'user_id' with the ID of the user you want to delete
    user_id = 'user_id'
    response = client.delete(f'/api/admin/user/{user_id}')
    assert response.status_code == 200

def test_delete_property(client):
    # Replace 'property_id' with the ID of the property you want to delete
    property_id = 'property_id'
    response = client.delete(f'/api/admin/property/{property_id}')
    assert response.status_code == 200

# Add more test cases as needed

