from flask import Flask, session, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import config
import pyrebase


app = Flask(__name__)


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app.secret_key = 'secret'

@app.route('/', methods =['POST', 'GET'])
def home():
    if('user' in session):
        return 'Hi, {} </br><a href="/logout"><button>logout</button></a>'.format(session['user'])
    
    if request.method == 'POST':
        email =request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return 'failed'
    return render_template('home.html')

@app.route('/signup', methods =['POST', 'GET'])
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

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')




if __name__ == '__main__':
    app.run(port=1111)