from flask import Blueprint, render_template

alumni = Blueprint('alumni' , __name__)


@alumni.route('/alumni')
def alumni_home():
    return render_template('alumni.html')
