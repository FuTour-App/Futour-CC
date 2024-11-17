from flask import Flask
from flask_login import LoginManager
from flask_session import Session
from api.routes.auth import auth_bp
from api.models.user import User
from typing import Optional

login_manager = LoginManager()
session = Session()

@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.get_by_id(user_id)

def create_app(config_file: str = '../config.py') -> Flask:
    """
    Args:
        config_file: Path to configuration file 
    Returns:
        Configured Flask application instance
    """
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    app.secret_key = app.config['SECRET_KEY']
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    session.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app
