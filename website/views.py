from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import PInfo, User, Trips
import datetime, json
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
#"<h1>Test</h1>"

@views.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    if request.method == 'POST':
        birthday = datetime.datetime.strptime(request.form['birthday'], "%Y-%m-%d")
        location = request.form.get('city')
        gender = request.form.get('gender')
        preferences = json.dumps(request.form.getlist('preferences[]'))
        diet = request.form.get('diet')

        new_pinfo= PInfo(
            user_id = current_user.id, 
            birthday=birthday,
            location=location, 
            gender=gender, 
            preferences=preferences,
            diet=diet
        )
        db.session.add(new_pinfo)
        db.session.commit()

        return redirect(url_for('views.dashboard'))



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

@views.route('/create_new',  methods=['GET', 'POST'])
def create_new():
    print(request.method)
    if request.method == 'POST':
        tripName = request.form.get('tripName')
        startDate = datetime.datetime.strptime(request.form['startDate'], "%Y-%m-%d")
        endDate = datetime.datetime.strptime(request.form['endDate'], "%Y-%m-%d")
        location = request.form.get('location')
        tripType = request.form.get('tripType')
        budget = request.form.get('budget')
        groupLeader_id = current_user.id
        groupLeader_name = current_user.first_name

        print(tripName)
        print(startDate)
        print(endDate)
        print(location)
        print(tripType)
        print(budget)
        print(groupLeader_id)
        print(groupLeader_name)

        new_trip= Trips(
            tripName = tripName,
            groupLeader_id=groupLeader_id,
            groupLeader_name=groupLeader_name, 
            startDate=startDate, 
            endDate=endDate,
            location=location,
            tripType=tripType,
            budget=budget
        )

        print(tripName)
        print(startDate)
        print(endDate)
        print(location)
        print(tripType)
        print(budget)
        print(groupLeader_id)
        print(groupLeader_name)

        db.session.add(new_trip)
        db.session.commit()
        return redirect(url_for('views.trip_detail', trip_id=new_trip.id))
    return render_template("create_new.html", user=current_user)
#"<h1>Test</h1>"

@views.route('/join_group')
def join_group():
    return render_template("join_group.html")

@views.route('/join_group_display')
def join_group_display():
    return render_template("join_group_display.html")


@views.route('/trip/<int:trip_id>')
def trip_detail(trip_id):
    trip = Trips.query.get_or_404(trip_id)
    return render_template('trip.html', trip=trip)
