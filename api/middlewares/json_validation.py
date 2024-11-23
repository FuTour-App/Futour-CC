from functools import wraps
from flask import request, jsonify
from http import HTTPStatus

def validate_json():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not request.is_json:
                return jsonify({
                    'status': 'error',
                    'message': 'Content-Type must be application/json'
                }), HTTPStatus.BAD_REQUEST
            return f(*args, **kwargs)
        return decorated_function
    return decorator
