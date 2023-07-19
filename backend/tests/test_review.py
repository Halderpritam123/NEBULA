import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_create_review(client):
    data = {
        'property_id': 'property_id',  # Replace with the ID of the property for which you want to add a review
        'rating': 4.5,
        'comment': 'Great place to stay!'
    }
    response = client.post('/api/review', json=data)
    assert response.status_code == 201

def test_get_review(client):
    # Replace 'review_id' with the ID of the review you want to retrieve
    review_id = 'review_id'
    response = client.get(f'/api/review/{review_id}')
    assert response.status_code == 200

def test_get_reviews_for_property(client):
    # Replace 'property_id' with the ID of the property for which you want to fetch reviews
    property_id = 'property_id'
    response = client.get(f'/api/reviews/property/{property_id}')
    assert response.status_code == 200

def test_update_review(client):
    # Replace 'review_id' with the ID of the review you want to update
    review_id = 'review_id'
    data = {
        'rating': 5.0,
        'comment': 'Awesome place!'
    }
    response = client.put(f'/api/review/{review_id}', json=data)
    assert response.status_code == 200

def test_delete_review(client):
    # Replace 'review_id' with the ID of the review you want to delete
    review_id = 'review_id'
    response = client.delete(f'/api/review/{review_id}')
    assert response.status_code == 204

# Add more test cases as needed

