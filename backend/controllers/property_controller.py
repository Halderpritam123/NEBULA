from app.models import Property, Booking, Review
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

def get_all_properties():
    properties = Property.objects()
    return jsonify(properties), 200

def get_property(property_id):
    property = Property.objects(id=property_id).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404
    return jsonify(property), 200

def create_property():
    title = request.json.get('title')
    description = request.json.get('description')
    location = request.json.get('location')
    price = request.json.get('price')
    # Add more property fields as needed

    if not title or not description or not location or not price:
        return jsonify({'error': 'Title, description, location, and price are required.'}), 400

    current_user_id = get_jwt_identity()
    property = Property(title=title, description=description, location=location, price=price, host_id=current_user_id)
    # Create more property fields as needed

    # Save the property to the database
    property.save()

    return jsonify({'message': 'Property created successfully.', 'property_id': str(property.id)}), 201

def update_property(property_id):
    current_user_id = get_jwt_identity()
    property = Property.objects(id=property_id).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    # Check if the current user is the host of the property
    if str(property.host_id) != current_user_id:
        return jsonify({'error': 'You are not authorized to update this property.'}), 403

    # Update property fields based on the request data
    title = request.json.get('title')
    description = request.json.get('description')
    location = request.json.get('location')
    price = request.json.get('price')
    # Add more property fields as needed

    if not title or not description or not location or not price:
        return jsonify({'error': 'Title, description, location, and price are required.'}), 400

    # Update the property fields
    property.title = title
    property.description = description
    property.location = location
    property.price = price
    # Update more property fields as needed

    # Save the updated property
    property.save()

    return jsonify({'message': 'Property updated successfully.', 'property_id': str(property.id)}), 200

def delete_property(property_id):
    current_user_id = get_jwt_identity()
    property = Property.objects(id=property_id).first()
    if not property:
        return jsonify({'error': 'Property not found.'}), 404

    # Check if the current user is the host of the property
    if str(property.host_id) != current_user_id:
        return jsonify({'error': 'You are not authorized to delete this property.'}), 403

    # Delete the property
    property.delete()

    return jsonify({'message': 'Property deleted successfully.'}), 200

# Add other property-related functions as needed
