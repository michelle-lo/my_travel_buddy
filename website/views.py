from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
#"<h1>Test</h1>"

@views.route('/personal_info')
def personal_info():
    return render_template("get_personal_info.html")
#"<h1>Test</h1>"

@login_required
@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", user=current_user)
#"<h1>Test</h1>"

@views.route('/new_trip')
def new_trip():
    return render_template("new_trip.html")
#"<h1>Test</h1>"

@views.route('/profile')
def profile():
    return render_template("profile.html")
#"<h1>Test</h1>"

@views.route('/profile_settings')
def profile_settings():
    return render_template("profile_settings.html")
#"<h1>Test</h1>"

@views.route('/trip')
def trip():
    return render_template("trip.html")
