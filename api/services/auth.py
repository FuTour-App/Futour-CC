from flask import session, render_template, request, redirect, url_for, flash
from typing import Union
from flask.wrappers import Response
from api.utils.firebase import auth, db
from api.models.user import User
from flask_login import login_user

class AuthService:
    def login(self) -> Union[str, Response]:
        if request.method == 'POST':
            email: str = request.form.get('email', '')
            password: str = request.form.get('password', '')
            
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user_id = user['localId']
                user_obj = User.get_by_id(user_id)
                
                if not user_obj:
                    raise ValueError("User not found in database")
                
                login_user(user_obj)

                session['user'] = {
                    "id": user_id,
                    "email": user_obj.email,
                    "username": user_obj.username
                }
                return redirect(url_for('auth.dashboard'))
            except Exception as e:
                flash(f"Login failed: {str(e)}", 'error')
                return render_template('auth/login.html')
                
        return render_template('auth/login.html')

    def signup(self) -> Union[str, Response]:
        if request.method == 'POST':
            username: str = request.form.get('username', '')
            email: str = request.form.get('email', '')
            password: str = request.form.get('password', '')
            
            try:
                user = auth.create_user_with_email_and_password(email, password)
                user_id = user['localId']
                
                new_user = User(user_id, username, email)
                db.child("users").child(user_id).set({
                    "username": new_user.username,
                    "email": new_user.email
                })
                flash('Account created successfully!', 'success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                flash(f"Signup failed: {str(e)}", 'error')
                return render_template('auth/signup.html')
                
        return render_template('auth/signup.html')

    def dashboard(self) -> Union[str, Response]:
        if 'user' not in session:
            return redirect(url_for('auth.login'))
            
        username = session['user']['username']
        return render_template('auth/dashboard.html', username=username)

    def logout(self) -> Union[str, Response]:
        if 'user' not in session:
            return {'error': 'Not logged in'}, 401
            
        session.pop('user')
        return redirect(url_for('auth.login'))