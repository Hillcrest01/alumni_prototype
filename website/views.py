from flask import Blueprint, render_template, session
from .models import Jobs, Events, Scholarships, Files, Gallery, Blog,User
from flask_login import login_required, current_user

views = Blueprint('views' , __name__)

@views.route('/', methods = ['POST' , 'GET'])
def home():
    jobs = Jobs.query.all()
    events = Events.query.all()
    members = User.query.count()
    event = Events.query.count()
    internship = Jobs.query.count()
    scholarship = Scholarships.query.count()

    return render_template('home.html' , jobs = jobs, events = events, members = members, event = event, scholarship=scholarship, internship = internship)

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


@views.route('/profile')
@login_required
def profile():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    return render_template('profile.html' , user = current_user)

@views.route('/download_report')
@login_required
def download_report():
    return render_template('download_report.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')


@views.route('/blogs')
def all_blogs():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).all()  # Fetch all blogs
    return render_template('blogs.html', blogs=blogs)

@views.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)  # Fetch the specific blog
    return render_template('blog_detail.html', blog=blog)

@views.route('/user/<int:user_id>')
def user_profile(user_id):
    user = User.query.get_or_404(user_id)  # Fetch user details
    blogs = Blog.query.filter_by(user_id=user.id).all()  # Get user blogs
    return render_template('blogger.html', user=user, blogs=blogs)
