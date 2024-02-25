from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
#"<h1>Test</h1>"

@views.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'POST':
        bdate = request.form.get('birthday')
        city = request.form.get('city')
        gender = request.form.get('gender')
        preferences = request.form.getlist('preferences[]')
        diet = request.form.get('diet')
        print(bdate)
        print(city)
        print(gender)
        print(preferences)
        print(diet)

    return render_template("get_personal_info.html", user=current_user)
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

@views.route('/create_new')
def create_new():
    return render_template("create_new.html")
#"<h1>Test</h1>"
