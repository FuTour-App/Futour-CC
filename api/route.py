from flask import Flask,Blueprint, session, render_template, request, redirect
from api.firebase_config import auth

route_blueprint = Blueprint('route_blueprint', __name__)
app = Flask(__name__, template_folder='template')
@route_blueprint.route('/', methods =['POST', 'GET'])
def home():
    if('user' in session):
       # return 'Hi, {} </br><a href="/logout"><button>logout</button></a>'.format(session['user'])
       username = session['user']
       return render_template('dashboard.html', u=username)
    
    if request.method == 'POST':
        email =request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return 'failed'
    return render_template('home.html')

@route_blueprint.route('/signup', methods =['POST', 'GET'])
def signup():
    
    if request.method == 'POST':
        email =request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            
            return redirect('/')
        except:
            return 'failed'
    return render_template('signup.html')

@route_blueprint.route('/logout')
def logout():
    if('user' in session):
        session.pop('user')
        return redirect('/')
    else:
        return 'login first to logout, please'
