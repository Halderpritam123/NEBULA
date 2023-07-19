import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_create_property(client):
    data = {
        'name': 'Cozy Apartment',
        'description': 'A cozy apartment in the city center',
        'price': 100,
        'location': 'City Center',
        'rating': 4.5
    }
    response = client.post('/api/property', json=data)
    assert response.status_code == 201

def test_get_property(client):
    # Replace 'property_id' with the ID of the property you want to retrieve
    property_id = 'property_id'
    response = client.get(f'/api/property/{property_id}')
    assert response.status_code == 200

def test_get_properties(client):
    response = client.get('/api/properties')
    assert response.status_code == 200

def test_update_property(client):
    # Replace 'property_id' with the ID of the property you want to update
    property_id = 'property_id'
    data = {
        'name': 'Updated Apartment',
        'price': 120
    }
    response = client.put(f'/api/property/{property_id}', json=data)
    assert response.status_code == 200

def test_delete_property(client):
    # Replace 'property_id' with the ID of the property you want to delete
    property_id = 'property_id'
    response = client.delete(f'/api/property/{property_id}')
    assert response.status_code == 204

# Add more test cases as needed

