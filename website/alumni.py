from flask import Blueprint, url_for, render_template, redirect

alumni = Blueprint('alumni' , __name__)


@alumni.route('/alumni')
def alumni_home():
    return render_template('alumni.html')
