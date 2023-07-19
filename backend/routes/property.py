from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Property, Review, Booking
from utils.validation_utils import validate_property_data, validate_review_data

property_bp = Blueprint('property', __name__)

@property_bp.route('/api/property', methods=['POST'])
@jwt_required()
def create_property():
    data = request.get_json()
    host_id = get_jwt_identity()

    # Validate property data
    validation_result = validate_property_data(data)
    if validation_result['error']:
        return jsonify(validation_result), 400

    property = Property(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        price=data['price'],
        capacity=data['capacity'],
        host=host_id
    )

    property.save()

    return jsonify({'message': 'Property created successfully'}), 201

@property_bp.route('/api/property/<string:property_id>', methods=['GET'])
def get_property(property_id):
    property = Property.objects.get_or_404(id=property_id)

    property_data = {
        'id': str(property.id),
        'title': property.title,
        'description': property.description,
        'location': property.location,
        'price': property.price,
        'capacity': property.capacity,
        'host_id': str(property.host.id),
        'created_at': property.created_at
    }

    return jsonify(property_data), 200

@property_bp.route('/api/properties', methods=['GET'])
def get_properties():
    properties = Property.objects.all()

    property_list = []

    for property in properties:
        property_data = {
            'id': str(property.id),
            'title': property.title,
            'description': property.description,
            'location': property.location,
            'price': property.price,
            'capacity': property.capacity,
            'host_id': str(property.host.id),
            'created_at': property.created_at
        }
        property_list.append(property_data)

    return jsonify(property_list), 200

@property_bp.route('/api/property/<string:property_id>', methods=['PUT'])
@jwt_required()
def update_property(property_id):
    data = request.get_json()
    host_id = get_jwt_identity()

    property = Property.objects.get_or_404(id=property_id)

    if str(property.host.id) != host_id:
        return jsonify({'error': 'Unauthorized'}), 401

    # Validate property data
    validation_result = validate_property_data(data)
    if validation_result['error']:
        return jsonify(validation_result), 400

    property.update(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        price=data['price'],
        capacity=data['capacity']
    )

    return jsonify({'message': 'Property updated successfully'}), 200

@property_bp.route('/api/property/<string:property_id>', methods=['DELETE'])
@jwt_required()
def delete_property(property_id):
    host_id = get_jwt_identity()

    property = Property.objects.get_or_404(id=property_id)

    if str(property.host.id) != host_id:
        return jsonify({'error': 'Unauthorized'}), 401

    property.delete()

    return jsonify({'message': 'Property deleted successfully'}), 200

@property_bp.route('/api/properties/search', methods=['GET'])
def search_properties():
    location = request.args.get('location')
    check_in_date = request.args.get('check_in_date')
    check_out_date = request.args.get('check_out_date')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    min_capacity = request.args.get('min_capacity')
    max_capacity = request.args.get('max_capacity')

    query = {}

    if location:
        query['location__icontains'] = location

    if check_in_date and check_out_date:
        # You can implement a check for available properties based on booking dates
        pass

    if min_price:
        query['price__gte'] = int(min_price)

    if max_price:
        query['price__lte'] = int(max_price)

    if min_capacity:
        query['capacity__gte'] = int(min_capacity)

    if max_capacity:
        query['capacity__lte'] = int(max_capacity)

    properties = Property.objects(**query)

    property_list = []

    for property in properties:
        property_data = {
            'id': str(property.id),
            'title': property.title,
            'description': property.description,
            'location': property.location,
            'price': property.price,
            'capacity': property.capacity,
            'host_id': str(property.host.id),
            'created_at': property.created_at
        }
        property_list.append(property_data)

    return jsonify(property_list), 200

@property_bp.route('/api/properties/sort', methods=['GET'])
def sort_properties():
    sort_by = request.args.get('sort_by')

    if sort_by not in ['price', 'ratings', 'criteria']:
        return jsonify({'error': 'Invalid sorting criteria'}), 400

    properties = Property.objects.order_by(sort_by)

    property_list = []

    for property in properties:
        property_data = {
            'id': str(property.id),
            'title': property.title,
            'description': property.description,
            'location': property.location,
            'price': property.price,
            'capacity': property.capacity,
            'host_id': str(property.host.id),
            'created_at': property.created_at
        }
        property_list.append(property_data)

    return jsonify(property_list), 200
