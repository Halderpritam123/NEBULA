import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_create_booking(client):
    # Replace 'property_id' with the ID of the property you want to book
    property_id = 'property_id'
    data = {
        'check_in_date': '2023-07-30',
        'check_out_date': '2023-08-06',
        'guests': 2
    }
    response = client.post(f'/api/booking/{property_id}', json=data)
    assert response.status_code == 201

def test_get_booking_details(client):
    # Replace 'booking_id' with the ID of the booking you want to retrieve
    booking_id = 'booking_id'
    response = client.get(f'/api/booking/{booking_id}')
    assert response.status_code == 200

def test_get_user_bookings(client):
    # Replace 'user_id' with the ID of the user whose bookings you want to retrieve
    user_id = 'user_id'
    response = client.get(f'/api/bookings/user/{user_id}')
    assert response.status_code == 200

def test_get_host_bookings(client):
    # Replace 'host_id' with the ID of the host whose bookings you want to retrieve
    host_id = 'host_id'
    response = client.get(f'/api/bookings/host/{host_id}')
    assert response.status_code == 200

def test_update_booking(client):
    # Replace 'booking_id' with the ID of the booking you want to update
    booking_id = 'booking_id'
    data = {
        'check_in_date': '2023-07-31',
        'check_out_date': '2023-08-05',
        'guests': 3
    }
    response = client.put(f'/api/booking/{booking_id}', json=data)
    assert response.status_code == 200

def test_cancel_booking(client):
    # Replace 'booking_id' with the ID of the booking you want to cancel
    booking_id = 'booking_id'
    response = client.delete(f'/api/booking/{booking_id}')
    assert response.status_code == 200

# Add more test cases as needed

