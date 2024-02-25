from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # date = db.Column(db.DataTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # one user to many notes, user = User


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note') #Note is the other class, capital needed
    pinfo = db.relationship('PInfo')
    trips = db.relationship('Trips')

    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, password={self.password}, first_name={self.first_name}, last_name={self.last_name})"
    
class PInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    birthday = db.Column(db.Date)
    location = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    preferences = db.Column(db.Text)
    diet = db.Column(db.String(20))


class Trips(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, autoincrement_start=1000)
    tripName = db.Column(db.String(100))
    groupLeader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    groupLeader_name = db.Column(db.String(100))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    location = db.Column(db.String(100))
    tripType = db.Column(db.String(100))
    budget = db.Column(db.BigInteger())
    participants = db.relationship('User', secondary='trip_participants', backref='trips_joined')

trip_participants = db.Table('trip_participants',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('trip_id', db.Integer, db.ForeignKey('trips.id'), primary_key=True)
)

