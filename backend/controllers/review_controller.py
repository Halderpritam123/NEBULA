from app.models import Review, Property
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

def get_reviews_for_property(property_id):
    property = Property.objects(id=property_id).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    reviews = Review.objects(property=property)
    return jsonify(reviews), 200

def create_review(property_id):
    property = Property.objects(id=property_id).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    current_user_id = get_jwt_identity()
    user_review = Review.objects(property=property, reviewer_id=current_user_id).first()
    if user_review:
        return jsonify({'error': 'You have already reviewed this property.'}), 400

    rating = request.json.get('rating')
    comment = request.json.get('comment')

    if not rating or not comment:
        return jsonify({'error': 'Rating and comment are required.'}), 400

    review = Review(property=property, reviewer_id=current_user_id, rating=rating, comment=comment)
    review.save()

    return jsonify({'message': 'Review added successfully.', 'review_id': str(review.id)}), 201

def delete_review(review_id):
    current_user_id = get_jwt_identity()
    review = Review.objects(id=review_id).first()
    if not review:
        return jsonify({'error': 'Review not found.'}), 404

    # Check if the current user is the reviewer of the review
    if str(review.reviewer_id) != current_user_id:
        return jsonify({'error': 'You are not authorized to delete this review.'}), 403

    # Delete the review
    review.delete()

    return jsonify({'message': 'Review deleted successfully.'}), 200

# Add other review-related functions as needed
