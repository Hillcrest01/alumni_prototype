from flask import Blueprint, render_template
from .models import Jobs

views = Blueprint('views' , __name__)

@views.route('/', methods = ['POST' , 'GET'])
def home():
    jobs = Jobs.query.all()
    return render_template('home.html' , jobs = jobs)