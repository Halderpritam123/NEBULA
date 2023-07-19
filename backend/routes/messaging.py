from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Message
from utils.validation_utils import validate_message_data

messaging_bp = Blueprint('messaging', __name__)

@messaging_bp.route('/api/message/<string:receiver_id>', methods=['POST'])
@jwt_required()
def send_message(receiver_id):
    data = request.get_json()
    sender_id = get_jwt_identity()

    # Validate message data
    validation_result = validate_message_data(data)
    if validation_result['error']:
        return jsonify(validation_result), 400

    message = Message(
        sender=sender_id,
        receiver=receiver_id,
        content=data['content']
    )

    message.save()

    return jsonify({'message': 'Message sent successfully'}), 201

@messaging_bp.route('/api/messages/<string:user_id>', methods=['GET'])
@jwt_required()
def get_user_messages(user_id):
    current_user_id = get_jwt_identity()

    if user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    messages_sent = Message.objects(sender=user_id)
    messages_received = Message.objects(receiver=user_id)

    message_list = []

    for message in messages_sent:
        message_data = {
            'id': str(message.id),
            'sender_id': str(message.sender.id),
            'receiver_id': str(message.receiver.id),
            'content': message.content,
            'sent_at': message.created_at
        }
        message_list.append(message_data)

    for message in messages_received:
        message_data = {
            'id': str(message.id),
            'sender_id': str(message.sender.id),
            'receiver_id': str(message.receiver.id),
            'content': message.content,
            'sent_at': message.created_at
        }
        message_list.append(message_data)

    # Sort messages by sent_at in descending order
    message_list.sort(key=lambda x: x['sent_at'], reverse=True)

    return jsonify(message_list), 200

@messaging_bp.route('/api/messages/<string:user_id>/<string:other_user_id>', methods=['GET'])
@jwt_required()
def get_messages_between_users(user_id, other_user_id):
    current_user_id = get_jwt_identity()

    if user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    messages_sent = Message.objects(sender=user_id, receiver=other_user_id)
    messages_received = Message.objects(sender=other_user_id, receiver=user_id)

    message_list = []

    for message in messages_sent:
        message_data = {
            'id': str(message.id),
            'sender_id': str(message.sender.id),
            'receiver_id': str(message.receiver.id),
            'content': message.content,
            'sent_at': message.created_at
        }
        message_list.append(message_data)

    for message in messages_received:
        message_data = {
            'id': str(message.id),
            'sender_id': str(message.sender.id),
            'receiver_id': str(message.receiver.id),
            'content': message.content,
            'sent_at': message.created_at
        }
        message_list.append(message_data)

    # Sort messages by sent_at in ascending order
    message_list.sort(key=lambda x: x['sent_at'])

    return jsonify(message_list), 200
