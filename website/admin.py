from flask import Blueprint

admin = Blueprint('admin' , __name__)

#Jobs
@admin.route('/add_job')
def add_job():
    pass

@admin.route('/edit_job')
def edit_job():
    pass

@admin.route('/delete_job')
def delete_job():
    pass


#events
@admin.route('/add_event')
def add_event():
    pass

@admin.route('/edit_event')
def edit_event():
    pass

@admin.route('/delete_event')
def delete_event():
    pass


#Scholarships

@admin.route('/add_scholarship')
def add_scholarship():
    pass

@admin.route('/edit_scholarship')
def edit_scholarship():
    pass

@admin.route('/delete_scholarship')
def delete_scholarship():
    pass

@admin.route('/add_jobs')
def add_jobs():
    pass

@admin.route('/edit_jobs')
def edit_jobs():
    pass

@admin.route('/delete_job')
def delete_job():
    pass

#learning materials
@admin.route('/add_file')
def add_file():
    pass

@admin.route('/edit_file')
def edit_file():
    pass

@admin.route('/delete_file')
def delete_file():
    pass

#blogs
@admin.route('/add_blog')
def add_blog():
    pass

@admin.route('/edit_blog')
def edit_blog():
    pass

@admin.route('/delete_blog')
def delete_blog():
    pass





