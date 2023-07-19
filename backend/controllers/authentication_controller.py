from app.models import User
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def signup():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid request data'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Username, email, and password are required'}), 400

    existing_user = User.objects(email=email).first()

    if existing_user:
        return jsonify({'message': 'Email already registered'}), 409

    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_password)
    user.save()

    return jsonify({'message': 'User created successfully'}), 201

def login():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid request data'}), 400

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    user = User.objects(email=email).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))

    return jsonify({'access_token': access_token}), 200

@jwt_required()
def get_user_profile():
    current_user_id = get_jwt_identity()
    user = User.objects(id=current_user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_data = {
        'id': str(user.id),
        'username': user.username,
        'email': user.email
    }

    return jsonify(user_data), 200

@jwt_required()
def update_user_profile():
    current_user_id = get_jwt_identity()
    user = User.objects(id=current_user_id).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.get_json()

    if not data:
        return jsonify({'message': 'Invalid request data'}), 400

    new_username = data.get('username')
    new_email = data.get('email')

    if new_username:
        user.username = new_username

    if new_email:
        user.email = new_email

    user.save()

    return jsonify({'message': 'User profile updated successfully'}), 200
