from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, login_user, logout_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    response = register_user(data)
    return jsonify(response)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    response = login_user(data)
    return jsonify(response)

@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = logout_user()
    return jsonify(response)

