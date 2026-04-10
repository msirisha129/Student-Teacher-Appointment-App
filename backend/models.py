from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))  # student / teacher / admin

class TeacherAvailability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    is_booked = db.Column(db.Boolean, default=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    status = db.Column(db.String(20), default="pending")
    remarks = db.Column(db.String(200))