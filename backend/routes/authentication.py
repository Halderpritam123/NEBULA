from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from utils.authentication_utils import generate_token, hash_password, check_password

authentication_bp = Blueprint('authentication', __name__)

@authentication_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.objects(email=email).first()
    if user:
        return jsonify({'error': 'Email already exists'}), 400

    hashed_password = hash_password(password)
    new_user = User(email=email, password=hashed_password)
    new_user.save()

    return jsonify({'message': 'User successfully registered'}), 201

@authentication_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    user = User.objects(email=email).first()
    if not user or not check_password(password, user.password):
        return jsonify({'error': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({'access_token': access_token}), 200

@authentication_bp.route('/api/user/profile', methods=['GET'])
@jwt_required()
def get_user_profile():
    user_id = get_jwt_identity()
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'email': user.email,
        'name': user.name,
        'phone': user.phone
    }), 200

@authentication_bp.route('/api/user/profile', methods=['PUT'])
@jwt_required()
def update_user_profile():
    user_id = get_jwt_identity()
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')

    if name:
        user.name = name
    if phone:
        user.phone = phone

    user.save()

    return jsonify({'message': 'Profile updated successfully'}), 200
