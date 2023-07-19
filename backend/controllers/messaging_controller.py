from app.models import User, Message
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

def send_message():
    current_user_id = get_jwt_identity()
    receiver_id = request.json.get('receiver_id')
    message_body = request.json.get('message_body')

    if not receiver_id or not message_body:
        return jsonify({'error': 'Receiver ID and message body are required.'}), 400

    # Check if the receiver exists
    receiver = User.objects(id=receiver_id).first()
    if not receiver:
        return jsonify({'error': 'Receiver not found.'}), 404

    # Create and save the message
    message = Message(
        sender_id=ObjectId(current_user_id),
        receiver_id=ObjectId(receiver_id),
        body=message_body
    )
    message.save()

    return jsonify({'message': 'Message sent successfully.'}), 200

def get_user_messages():
    current_user_id = get_jwt_identity()

    # Get all messages for the current user
    messages = Message.objects(receiver_id=ObjectId(current_user_id)).order_by('-timestamp')

    # Convert messages to JSON format
    messages_data = []
    for message in messages:
        messages_data.append({
            'id': str(message.id),
            'sender_id': str(message.sender_id),
            'receiver_id': str(message.receiver_id),
            'body': message.body,
            'timestamp': message.timestamp
        })

    return jsonify(messages_data), 200

def get_messages_between_users(user_id, other_user_id):
    current_user_id = get_jwt_identity()

    # Check if both users exist
    user = User.objects(id=user_id).first()
    other_user = User.objects(id=other_user_id).first()
    if not user or not other_user:
        return jsonify({'error': 'User(s) not found.'}), 404

    # Get all messages exchanged between the two users
    messages = Message.objects.filter(
        (Message.sender_id == ObjectId(current_user_id) and Message.receiver_id == ObjectId(other_user_id)) |
        (Message.sender_id == ObjectId(other_user_id) and Message.receiver_id == ObjectId(current_user_id))
    ).order_by('-timestamp')

    # Convert messages to JSON format
    messages_data = []
    for message in messages:
        messages_data.append({
            'id': str(message.id),
            'sender_id': str(message.sender_id),
            'receiver_id': str(message.receiver_id),
            'body': message.body,
            'timestamp': message.timestamp
        })

    return jsonify(messages_data), 200
