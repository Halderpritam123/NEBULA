from app.models import User, Property, Booking
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from bson import ObjectId 

def create_booking():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid request data'}), 400

    property_id = data.get('property_id')
    check_in_date = data.get('check_in_date')
    check_out_date = data.get('check_out_date')

    if not property_id or not check_in_date or not check_out_date:
        return jsonify({'message': 'Property ID, check-in date, and check-out date are required'}), 400

    try:
        property_id = ObjectId(property_id)
    except:
        return jsonify({'message': 'Invalid property ID format'}), 400

    property = Property.objects(id=property_id).first()

    if not property:
        return jsonify({'message': 'Property not found'}), 404

    current_user_id = get_jwt_identity()
    user = User.objects(id=current_user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    booking = Booking(property=property, user=user, check_in_date=check_in_date, check_out_date=check_out_date)
    booking.save()

    return jsonify({'message': 'Booking created successfully'}), 201

@jwt_required()
def get_user_bookings():
    current_user_id = get_jwt_identity()
    user = User.objects(id=current_user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    bookings = Booking.objects(user=user)

    if not bookings:
        return jsonify({'message': 'No bookings found'}), 404

    booking_list = []
    for booking in bookings:
        booking_data = {
            'id': str(booking.id),
            'property_id': str(booking.property.id),
            'check_in_date': booking.check_in_date.strftime('%Y-%m-%d'),
            'check_out_date': booking.check_out_date.strftime('%Y-%m-%d')
        }
        booking_list.append(booking_data)

    return jsonify(booking_list), 200

@jwt_required()
def get_host_bookings():
    current_user_id = get_jwt_identity()
    user = User.objects(id=current_user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    properties = Property.objects(host=user)

    if not properties:
        return jsonify({'message': 'No properties found for the host'}), 404

    bookings = Booking.objects(property__in=properties)

    if not bookings:
        return jsonify({'message': 'No bookings found for the host'}), 404

    booking_list = []
    for booking in bookings:
        booking_data = {
            'id': str(booking.id),
            'property_id': str(booking.property.id),
            'check_in_date': booking.check_in_date.strftime('%Y-%m-%d'),
            'check_out_date': booking.check_out_date.strftime('%Y-%m-%d'),
            'guest_username': booking.user.username
        }
        booking_list.append(booking_data)

    return jsonify(booking_list), 200

@jwt_required()
def update_booking():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid request data'}), 400

    booking_id = data.get('booking_id')
    check_in_date = data.get('check_in_date')
    check_out_date = data.get('check_out_date')

    if not booking_id or (not check_in_date and not check_out_date):
        return jsonify({'message': 'Booking ID and at least one field (check-in date or check-out date) are required'}), 400

    try:
        booking_id = ObjectId(booking_id)
    except:
        return jsonify({'message': 'Invalid booking ID format'}), 400

    booking = Booking.objects(id=booking_id).first()

    if not booking:
        return jsonify({'message': 'Booking not found'}), 404

    if check_in_date:
        booking.check_in_date = check_in_date

    if check_out_date:
        booking.check_out_date = check_out_date

    booking.save()

    return jsonify({'message': 'Booking updated successfully'}), 200

@jwt_required()
def cancel_booking():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid request data'}), 400

    booking_id = data.get('booking_id')

    if not booking_id:
        return jsonify({'message': 'Booking ID is required'}), 400

    try:
        booking_id = ObjectId(booking_id)
    except:
        return jsonify({'message': 'Invalid booking ID format'}), 400

    booking = Booking.objects(id=booking_id).first()

    if not booking:
        return jsonify({'message': 'Booking not found'}), 404

    booking.delete()

    return jsonify({'message': 'Booking canceled successfully'}), 200
