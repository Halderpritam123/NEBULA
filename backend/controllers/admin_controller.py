from app.models import User, Property, Booking
from bson.objectid import ObjectId

def get_all_users():
    users = User.objects()
    user_list = []

    for user in users:
        user_data = {
            'id': str(user.id),
            'username': user.username,
            'email': user.email,
            'is_host': user.is_host,
            'is_admin': user.is_admin,
            'is_verified': user.is_verified
        }
        user_list.append(user_data)

    return user_list

def get_all_properties():
    properties = Property.objects()
    property_list = []

    for property in properties:
        property_data = {
            'id': str(property.id),
            'title': property.title,
            'description': property.description,
            'price': property.price,
            'location': property.location,
            'rating': property.rating,
            'is_available': property.is_available,
            'host_id': str(property.host_id),
            'created_at': property.created_at
        }
        property_list.append(property_data)

    return property_list

def get_all_bookings():
    bookings = Booking.objects()
    booking_list = []

    for booking in bookings:
        booking_data = {
            'id': str(booking.id),
            'user_id': str(booking.user_id),
            'property_id': str(booking.property_id),
            'check_in_date': booking.check_in_date,
            'check_out_date': booking.check_out_date,
            'status': booking.status,
            'total_price': booking.total_price,
            'created_at': booking.created_at
        }
        booking_list.append(booking_data)

    return booking_list

def update_user_verification(user_id, is_verified):
    user = User.objects(id=user_id).first()

    if not user:
        return None

    user.is_verified = is_verified
    user.save()

    return user

def delete_user(user_id):
    user = User.objects(id=user_id).first()

    if not user:
        return None

    user.delete()

    return user

def delete_property(property_id):
    property = Property.objects(id=property_id).first()

    if not property:
        return None

    property.delete()

    return property
