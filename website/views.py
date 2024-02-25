from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import PInfo, User, Trips, trip_participants
import datetime, json
from . import db
from sqlalchemy.sql import select
#from website.AI_Generation.generate_gpt import gen_ai_plan

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
#"<h1>Test</h1>"

@views.route('/personal_info', methods=['GET', 'POST'])
def personal_info():
    stmt = select(PInfo).where(
        (PInfo.user_id == current_user.id) 
    )
    existing_pinfo = db.session.execute(stmt).fetchone()
    print(existing_pinfo)
    # if not existing_pinfo:
    if request.method == 'POST':
        stmt = select(PInfo).where(
            (PInfo.user_id == current_user.id) 
        )
        existing_pinfo = db.session.execute(stmt).fetchone()
        if not existing_pinfo:
            
            birthday = datetime.datetime.strptime(request.form['birthday'], "%Y-%m-%d")
            location = request.form.get('city')
            gender = request.form.get('gender')
            preferences = json.dumps(request.form.getlist('preferences[]'))
            diet = request.form.get('diet')
            email = current_user.email

            new_pinfo= PInfo(
                user_id = current_user.id, 
                birthday=birthday,
                location=location, 
                gender=gender, 
                preferences=preferences,
                diet=diet,
                email=email
            )
            db.session.add(new_pinfo)
            db.session.commit()
        else:
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


@views.route('profile/<string:email>/')
def profile(email):
    user_info = PInfo.query.filter_by(email=email).first()
    user = User.query.filter_by(email=email).first()
    print(user.first_name)
    if user_info:
        return render_template('profile.html', 
            email = user_info.email,
            name = user.first_name + " " + user.last_name,
            birthday = user_info.birthday,
            location = user_info.location,
            gender = user_info.gender,
            preferences = user_info.preferences,
            diet = user_info.diet
        )
    else:
        # If user does not exist, handle accordingly (e.g., display an error message)
        return 'profile not found'
    
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

        db.session.add(new_trip)
        db.session.commit()

        return redirect(url_for('views.trip_detail', trip_id=new_trip.id))
    return render_template("create_new.html", user=current_user)
#"<h1>Test</h1>"

@views.route('/join_group', methods=['GET', 'POST'])
def join_group():
    if request.method == "POST":
        trip_id = request.form['trip_id']
        print(trip_id)
        trip = Trips.query.get(trip_id)
        if trip:
            return redirect(url_for('views.trip_detail', trip_id=trip.id))
        else:
            return "Trip ID does not exist."
    return render_template("join_group.html")

@views.route('/join_group_display', )
def join_group_display():
    return render_template("join_group_display.html")


@views.route('/trip/<int:trip_id>', methods=['GET', 'POST'])
def trip_detail(trip_id):
    if request.method == "POST":
        return redirect(url_for('views.gen_plan', trip_id=trip_id))
    trip = Trips.query.get_or_404(trip_id)
    stmt = select(trip_participants).where(
        (trip_participants.c.user_id == current_user.id) & (trip_participants.c.trip_id == trip.id)
    )
    existing_participant = db.session.execute(stmt).fetchone()
    if not existing_participant:
        new_participant = trip_participants.insert().values(user_id=current_user.id, trip_id=trip.id)
        db.session.execute(new_participant)
        db.session.commit()

    print(trip.participants)
    return render_template(
        'trip.html', 
        trip=trip,
        tripID = trip.id,
        groupLeader = trip.groupLeader_name,
        tripName = trip.tripName,
        startDate = trip.startDate,
        endDate = trip.endDate,
        location = trip.location,
        tripType = trip.tripType,
        budget = trip.budget
    )

    

@views.route('/trip/<int:trip_id>/plan', methods=['GET', 'POST'])
def gen_plan(trip_id):
    return "hello"
    #return gen_ai_plan(trip_id)