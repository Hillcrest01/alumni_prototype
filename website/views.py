from flask import Blueprint, render_template
from .models import Jobs, Events, Scholarships, Files, Gallery, Blog

views = Blueprint('views' , __name__)

@views.route('/', methods = ['POST' , 'GET'])
def home():
    jobs = Jobs.query.all()
    return render_template('home.html' , jobs = jobs)

@views.route('/jobs')
def jobs():
    jobs = Jobs.query.all()
    return render_template('jobs.html' , jobs = jobs)

@views.route('/events')
def events():
    events = Events.query.all()
    return render_template('events.html' , events = events)

@views.route('/scholarships')
def scholarships():
    scholarships = Scholarships.query.all()
    return render_template('scholarships.html' , scholarships = scholarships)

@views.route('/files')
def files():
    files = Files.query.all()
    return render_template('files.html' , files = files)

@views.route('/gallery')
def gallery():
    images = Gallery.query.all()
    return render_template('gallery.html' , images = images)

@views.route('/blogs')
def blogs():
    blogs = Blog.query.all()
    return render_template('blog.html' , blogs = blogs)