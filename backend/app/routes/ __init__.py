# In app/routes/__init__.py
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify(message='Hello, the backend is running!')

