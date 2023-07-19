from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

def generate_token(user_id):
    access_token = create_access_token(identity=user_id)
    return access_token

def hash_password(password):
    return generate_password_hash(password)

def check_password(user, password):
    return check_password_hash(user.password, password)

def get_current_user():
    current_user_id = get_jwt_identity()
    return User.objects(id=current_user_id).first() if current_user_id else None
