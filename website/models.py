from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    regno = db.Column(db.String(20))
    year_of_study = db.Column(db.Integer)
    email_address = db.Column(db.String(50))
    password_hash = db.Column(db.String(500))
    date_joined = db.Column(db.DateTime(), default  = datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    body = db.Column(db.String(1000) , nullable = False)
    location = db.Column(db.String(50) , nullable = False)
    job_type = db.Column(db.String(100) , nullable = False)
    link = db.Column(db.String(100) , nullable = False)
    image = db.Column(db.String(1000) , nullable = False)


class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    body = db.Column(db.String(1000) , nullable = False)
    location = db.Column(db.String(50) , nullable = False)
    link = db.Column(db.String(100) , nullable = False)
    image = db.Column(db.String(1000) , nullable = False)

class Scholarships(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100) , nullable = False)
    body = db.Column(db.String(1000) , nullable = False)
    country = db.Column(db.String(50) , nullable = False)
    university = db.Column(db.String(100) , nullable = False)
    link = db.Column(db.String(100) , nullable = False)
    image = db.Column(db.String(1000) , nullable = False)


class Files(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Integer, nullable = False)
    link = db.Column(db.String(100) , nullable = False)
    image = db.Column(db.String(1000) , nullable = False)

class Gallery(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    image = db.Column(db.String(1000) , nullable = False) 

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    body = db.Column(db.String(1000))
    image = db.Column(db.String(1000))


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)