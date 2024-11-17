from flask import Blueprint

admin = Blueprint('admin' , __name__)

@admin.route('/add_jobs')
def add_jobs():
    pass
