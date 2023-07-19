from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Booking
from utils.validation_utils import validate_booking_data

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/api/booking/<string:property_id>', methods=['POST'])
@jwt_required()
def create_booking(property_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    # Validate booking data
    validation_result = validate_booking_data(data)
    if validation_result['error']:
        return jsonify(validation_result), 400

    check_in_date = data['check_in_date']
    check_out_date = data['check_out_date']

    # Check if the property is available for booking on the specified dates
    existing_booking = Booking.objects(property=property_id, 
                                       check_in_date__lte=check_out_date, 
                                       check_out_date__gte=check_in_date).first()

    if existing_booking:
        return jsonify({'error': 'The property is not available for booking on the specified dates'}), 400

    # Create a new booking
    booking = Booking(
        user=user_id,
        property=property_id,
        check_in_date=check_in_date,
        check_out_date=check_out_date,
        guests=data['guests'],
        message=data.get('message')
    )

    booking.save()

    return jsonify({'message': 'Booking created successfully'}), 201

@booking_bp.route('/api/booking/<string:booking_id>', methods=['GET'])
@jwt_required()
def get_booking(booking_id):
    booking = Booking.objects(id=booking_id).first()
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    booking_data = {
        'id': str(booking.id),
        'user_id': str(booking.user.id),
        'property_id': str(booking.property.id),
        'check_in_date': booking.check_in_date,
        'check_out_date': booking.check_out_date,
        'guests': booking.guests,
        'message': booking.message
    }

    return jsonify(booking_data), 200

@booking_bp.route('/api/bookings/user', methods=['GET'])
@jwt_required()
def get_user_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.objects(user=user_id)
    booking_list = []

    for booking in bookings:
        booking_data = {
            'id': str(booking.id),
            'property_id': str(booking.property.id),
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date,
            'guests': booking.guests,
            'message': booking.message
        }
        booking_list.append(booking_data)

    return jsonify(booking_list), 200

@booking_bp.route('/api/bookings/host', methods=['GET'])
@jwt_required()
def get_host_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.objects(property__host=user_id)
    booking_list = []

    for booking in bookings:
        booking_data = {
            'id': str(booking.id),
            'user_id': str(booking.user.id),
            'property_id': str(booking.property.id),
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date,
            'guests': booking.guests,
            'message': booking.message
        }
        booking_list.append(booking_data)

    return jsonify(booking_list), 200

@booking_bp.route('/api/booking/<string:booking_id>', methods=['PUT'])
@jwt_required()
def update_booking(booking_id):
    booking = Booking.objects(id=booking_id).first()
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    data = request.get_json()
    check_in_date = data.get('check_in_date')
    check_out_date = data.get('check_out_date')
    guests = data.get('guests')
    message = data.get('message')

    if check_in_date:
        booking.check_in_date = check_in_date
    if check_out_date:
        booking.check_out_date = check_out_date
    if guests:
        booking.guests = guests
    if message:
        booking.message = message

    booking.save()

    return jsonify({'message': 'Booking updated successfully'}), 200

@booking_bp.route('/api/booking/<string:booking_id>', methods=['DELETE'])
@jwt_required()
def delete_booking(booking_id):
    booking = Booking.objects(id=booking_id).first()
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    booking.delete()

    return jsonify({'message': 'Booking deleted successfully'}), 200
