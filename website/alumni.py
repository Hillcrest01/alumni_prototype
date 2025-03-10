from flask import Blueprint, render_template
from .models import Jobs, Events, User, Scholarships

alumni = Blueprint('alumni' , __name__)


@alumni.route('/alumni')
def alumni_home():
    jobs = Jobs.query.all()
    events = Events.query.all()
    members = User.query.count()
    event = Events.query.count()
    internship = Jobs.query.count()
    scholarship = Scholarships.query.count()





    return render_template('alumni.html' , jobs=jobs, events=events, members=members, event=event, scholarship=scholarship, internship=internship)
