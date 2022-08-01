from pytz import timezone
from .import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), nullable=False,default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note', backref='user', lazy='dynamic')

    

