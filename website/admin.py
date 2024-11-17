from flask import Blueprint, request, render_template, redirect, url_for, send_from_directory, flash, get_flashed_messages
from . import db
from .models import Jobs, Events, Scholarships, Files, Gallery, Blog
from .forms import JobsForm, ScholarshipForm, EventForm, FilesForm, BlogForm, GalleryForm
from werkzeug.utils import secure_filename #used when dealing with images

admin = Blueprint('admin' , __name__)

#to deal with images, we define a route where the images will be stored.

@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory('../media/' , filename)

#Jobs
@admin.route('/add_job' , methods = ['POST' , 'GET'])
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        location = request.form.get("location")
        job_type = request.form.get("job_type")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            print('file received')
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            new_job = Jobs(title = title , body = body , location = location , job_type = job_type, link = link, image = file_path)
            db.session.add(new_job)
            db.session.commit()
            flash('job added successfully')
            print('successfully added the job')
            return redirect(url_for('views.home'))

        else:
            flash('job not added, please try again')
            print('job not added!!')

    return render_template('add_job.html' , form = form)


@admin.route('/edit_job/<int:job_id>' , methods = ['POST' , 'GET'])
def edit_job(job_id):
    job = Jobs.query.get_or_404(job_id)
    form = JobsForm(obj = job)

    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        location = request.form.get("location")
        job_type = request.form.get("job_type")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)
        Jobs.query.filter_by(id = job_id).update(dict(title = title , body = body , location = location , job_type = job_type, link = link, image = file_path))
        db.session.commit()
        flash('job successfully updated')
        print('job updated successful')
        return redirect(url_for('views.home'))

    else:
        print("item not updated")
    
    return render_template('edit_job.html' , form = form)


@admin.route('/delete_job/<int:job_id>' , methods = ['POST' , 'GET'])
def delete_job(job_id):
    job_to_delete = Jobs.query.get(job_id)
    db.session.delete(job_to_delete)
    db.session.commit()
    flash('job deleted successfully')
    print('successfully deleted job')
    return redirect(url_for('views.home'))


#events
@admin.route('/add_event' , methods = ['POST' , 'GET'])
def add_event():
    pass

@admin.route('/edit_event' , methods = ['POST' , 'GET'])
def edit_event():
    pass

@admin.route('/delete_event' , methods = ['POST' , 'GET'])
def delete_event():
    pass


#Scholarships

@admin.route('/add_scholarship' , methods = ['POST' , 'GET'])
def add_scholarship():
    pass

@admin.route('/edit_scholarship' , methods = ['POST' , 'GET'])
def edit_scholarship():
    pass

@admin.route('/delete_scholarship' , methods = ['POST' , 'GET'])
def delete_scholarship():
    pass

#blogs
@admin.route('/add_files' , methods = ['POST' , 'GET'])
def add_files():
    pass

@admin.route('/edit_files' , methods = ['POST' , 'GET'])
def edit_files():
    pass

@admin.route('/deletefiles' , methods = ['POST' , 'GET'])
def deletefiles():
    pass

#learning materials
@admin.route('/add_file' , methods = ['POST' , 'GET'])
def add_file():
    pass

@admin.route('/edit_file' , methods = ['POST' , 'GET'])
def edit_file():
    pass

@admin.route('/delete_file' , methods = ['POST' , 'GET'])
def delete_file():
    pass

#blogs
@admin.route('/add_blog' , methods = ['POST' , 'GET'])
def add_blog():
    pass

@admin.route('/edit_blog' , methods = ['POST' , 'GET'])
def edit_blog():
    pass

@admin.route('/delete_blog' , methods = ['POST' , 'GET'])
def delete_blog():
    pass





