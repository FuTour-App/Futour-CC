from flask import session, render_template, request, redirect
from api.firebase_config import auth, db

def home():
    if('user' in session):
       # return 'Hi, {} </br><a href="/logout"><button>logout</button></a>'.format(session['user'])
       username = session['user']['username']
       return render_template('dashboard.html', u=username)
    
    if request.method == 'POST':
        email =request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            user_id = user['localId']  
            
            user_data = db.child("users").child(user_id).get()
            username = user_data.val().get("username")
            
            session['user'] = {"email": email, "username": username}
        except:
            return 'failed'
    return render_template('home.html')

def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email =request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            user_id = user['localId']  

            db.child("users").child(user_id).set({
                "username": username,
                "email": email
            })
            return redirect('/')
        except:
            return 'failed'
    return render_template('signup.html')

def logout():
    if('user' in session):
        session.pop('user')
        return redirect('/')
    else:
        return 'login first to logout, please'


