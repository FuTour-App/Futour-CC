from flask import Blueprint
from flask_login import login_required
from api.services.auth import AuthService
from typing import Union
from flask.wrappers import Response

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST', 'GET'])
def login() -> Union[str, Response]:
    return auth_service.login()

@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup() -> Union[str, Response]:
    return auth_service.signup()

@auth_bp.route('/logout')
@login_required
def logout() -> Response:
    return auth_service.logout()

@auth_bp.route('/dashboard')
@login_required
def dashboard() -> Union[str, Response]:
    return auth_service.dashboard()
