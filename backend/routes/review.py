from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Property, Review
from utils.validation_utils import validate_review_data

review_bp = Blueprint('review', __name__)

@review_bp.route('/api/review/<string:property_id>', methods=['POST'])
@jwt_required()
def create_review(property_id):
    user_id = get_jwt_identity()
    property = Property.objects(id=property_id).first()

    if not property:
        return jsonify({'error': 'Property not found'}), 404

    data = request.get_json()

    # Validate the review data
    error_message = validate_review_data(data)
    if error_message:
        return jsonify({'error': error_message}), 400

    review = Review(
        user_id=user_id,
        property_id=property_id,
        rating=data['rating'],
        comment=data['comment']
    )
    review.save()

    return jsonify({'message': 'Review created successfully'}), 201

@review_bp.route('/api/review/<string:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.objects(id=review_id).first()

    if not review:
        return jsonify({'error': 'Review not found'}), 404

    review_data = {
        'id': str(review.id),
        'user_id': str(review.user_id),
        'property_id': str(review.property_id),
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at
    }

    return jsonify(review_data), 200

@review_bp.route('/api/reviews/property/<string:property_id>', methods=['GET'])
def get_reviews_for_property(property_id):
    property = Property.objects(id=property_id).first()

    if not property:
        return jsonify({'error': 'Property not found'}), 404

    reviews = Review.objects(property_id=property_id)

    review_list = []

    for review in reviews:
        review_data = {
            'id': str(review.id),
            'user_id': str(review.user_id),
            'property_id': str(review.property_id),
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at
        }
        review_list.append(review_data)

    return jsonify(review_list), 200
