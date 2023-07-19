import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_send_message(client):
    # Replace 'receiver_id' with the ID of the user who will receive the message
    receiver_id = 'receiver_id'
    data = {
        'message': 'Hello, this is a test message!'
    }
    response = client.post(f'/api/message/{receiver_id}', json=data)
    assert response.status_code == 201

def test_get_user_messages(client):
    # Replace 'user_id' with the ID of the user whose messages you want to retrieve
    user_id = 'user_id'
    response = client.get(f'/api/messages/{user_id}')
    assert response.status_code == 200

def test_get_messages_between_users(client):
    # Replace 'user_id1' and 'user_id2' with the IDs of the two users whose messages you want to retrieve
    user_id1 = 'user_id1'
    user_id2 = 'user_id2'
    response = client.get(f'/api/messages/{user_id1}/{user_id2}')
    assert response.status_code == 200

# Add more test cases as needed

