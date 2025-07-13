from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"msg": "Email is required"}), 400

    user = User.query.get(email)
    if not user:
        return jsonify({"msg": "User not authorized"}), 403

    token = create_access_token(identity=email)
    return jsonify(user=email, access_token=token)
