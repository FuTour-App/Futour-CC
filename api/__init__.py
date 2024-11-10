from flask import Flask
from api.firebase_config import auth
from api.route import route_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.register_blueprint(route_blueprint)
    
    return app
