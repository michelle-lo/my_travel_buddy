from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email)
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.dashboard'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            # user does not exist
            flash('Email does not exist', category='error')
    return render_template("login_page.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists", category='error')
        elif len(email) < 4:
            flash("Email invalid", category="error")
        elif len(first_name) < 2:
            flash("First name invalid", category="error")
        elif len(last_name) < 2:
            flash("Last name invalid", category="error")
        elif password1 != password2:
            flash("Passwords must match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            flash("Account created", category="success")
            #new_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            new_user = User(email=email, first_name=first_name, last_name=last_name, password=password1) #illegal haha
            db.session.add(new_user)
            db.session.commit()
                            
            return redirect(url_for('views.home'))

        
        
            #something happens
    
    return render_template("sign_up.html")

