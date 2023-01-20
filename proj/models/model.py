import uuid
from flask import json
from proj.models import db
import bcrypt

class User(db.Model):
    uuid = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    # age = db.Column(db.String(50))
    # date_birth = db.Column(db.DateTime)
    # gender = db.Column(db.String(50))

    def __init__(self, username, email, password):
        self.uuid = uuid.uuid4().hex
        self.username = username
        self.email = email
        
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode(), salt=salt) 
        # self.age = age
        # self.date_birth = date_births
        # self.gender = gender
