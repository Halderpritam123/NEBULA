from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User
from utils.authentication_utils import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/api/admin/users', methods=['GET'])
@jwt_required()
@admin_required
def get_all_users():
    users = User.objects()
    user_list = []
    for user in users:
        user_data = {
            'id': str(user.id),
            'email': user.email,
            'name': user.name,
            'phone': user.phone,
            'is_admin': user.is_admin
        }
        user_list.append(user_data)

    return jsonify(user_list), 200

@admin_bp.route('/api/admin/user/<string:user_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    is_admin = data.get('is_admin')

    if name:
        user.name = name
    if phone:
        user.phone = phone
    if is_admin is not None:
        user.is_admin = is_admin

    user.save()

    return jsonify({'message': 'User updated successfully'}), 200

@admin_bp.route('/api/admin/user/<string:user_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user(user_id):
    user = User.objects(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.delete()

    return jsonify({'message': 'User deleted successfully'}), 200
