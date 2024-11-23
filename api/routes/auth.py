from flask import Blueprint, request
from api.services.auth import AuthService
from typing import Tuple, Dict
from api.middlewares.json_validation import validate_json
from api.middlewares.auth import verify_token

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
@validate_json()
def login() -> Tuple[Dict, int]:
    data = request.get_json()
    return auth_service.login(data)

@auth_bp.route('/signup', methods=['POST'])
@validate_json()
def signup() -> Tuple[Dict, int]:
    data = request.get_json()
    return auth_service.signup(data)

@auth_bp.route('/logout', methods=['POST'])
@verify_token()
def logout() -> Tuple[Dict, int]:
    token = request.headers.get('Authorization').split(" ")[1]
    return auth_service.logout(token)

@auth_bp.route('/me', methods=['GET'])
@verify_token()
def get_current_user() -> Tuple[Dict, int]:
    token = request.headers.get('Authorization').split(" ")[1]
    return auth_service.get_current_user(token)