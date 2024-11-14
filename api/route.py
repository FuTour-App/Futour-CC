from flask import Flask,Blueprint, session, render_template, request, redirect
from api.firebase_config import auth
from api.services.auth import login, signup, logout, dashboard

route_blueprint = Blueprint('route_blueprint', __name__)
app = Flask(__name__, template_folder='template')

@route_blueprint.route('/login', methods =['POST', 'GET'])
def home_route():
        return login()

@route_blueprint.route('/signup', methods =['POST', 'GET'])
def signup_route():
        return signup()
   
@route_blueprint.route('/logout')
def logout_route():
    return logout()

@route_blueprint.route('/dashboard', methods = ['GET'])
def dashboard_route():
    return dashboard()