from flask import Blueprint, request, render_template, redirect, url_for, send_from_directory, flash, get_flashed_messages
from . import db
from .models import Jobs, Events, Scholarships, Files, Gallery, Blog
from .forms import JobsForm, ScholarshipForm, EventForm, FilesForm, BlogForm, GalleryForm
from werkzeug.utils import secure_filename #used when dealing with images

admin = Blueprint('admin' , __name__)

@admin.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')



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

#end of jobs, .....


#events
@admin.route('/add_event' , methods = ['POST' , 'GET'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        location = request.form.get("location")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            print('file received')
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            new_event = Events(title = title , body = body , location = location , link = link, image = file_path)
            db.session.add(new_event)
            db.session.commit()
            flash('event added successfully')
            print('successfully added the event')
            return redirect(url_for('views.home'))

        else:
            flash('event not added, please try again')
            print('event not added!!')

    return render_template('add_event.html' , form = form)

@admin.route('/edit_event/<int:event_id>' , methods = ['POST' , 'GET'])
def edit_event(event_id):
    event = Events.query.get_or_404(event_id)
    form = JobsForm(obj = event)

    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        location = request.form.get("location")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)
        Events.query.filter_by(id = event_id).update(dict(title = title , body = body , location = location , link = link, image = file_path))
        db.session.commit()
        flash('Events successfully updated')
        print('Events updated successful')
        return redirect(url_for('views.home'))

    else:
        print("event not updated")
    
    return render_template('edit_event.html' , form = form)


@admin.route('/delete_event/<int:event_id>' , methods = ['POST' , 'GET'])
def delete_event(event_id):
    event_to_delete = Events.query.get(event_id)
    db.session.delete(event_to_delete)
    db.session.commit()
    flash('event deleted successfully')
    print('event deleted')
    return redirect(url_for('views.home'))

#End of events



#Scholarships

@admin.route('/add_scholarship' , methods = ['POST' , 'GET'])
def add_scholarship():
    form = ScholarshipForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        country = request.form.get("country")
        university = request.form.get("university")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            new_scholarship = Scholarships(title = title, body = body, country = country, university = university, link = link, image = file_path)
            db.session.add(new_scholarship)
            db.session.commit()
            flash('new scholarship added successfully!')
            print('new scholarship added successfully')
            return redirect(url_for('views.home'))
        
        else:
            print('scholarship not added, please try again')
            flash('scholarship not added, please try again')


    
    return render_template('add_scholarship.html' , form = form)



@admin.route('/edit_scholarship/<int:scholarship_id>' , methods = ['POST' , 'GET'])
def edit_scholarship(scholarship_id):
    scholarships = Scholarships.query.get_or_404(scholarship_id)
    form = ScholarshipForm(obj = scholarships)
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        country = request.form.get("country")
        university = request.form.get("university")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)
            Scholarships.query.filter_by(id = scholarship_id).update(dict(title = title, body = body, country = country, university = university, link = link, image = file_path))
            db.session.commit()
            flash('scholarship successfully updated')
            print("successfully updated")
            return redirect(url_for('views.home'))
        

        else:
            flash('scholarship not updated, pleas try again')
            print('scholarship not updated!')

        return render_template('edit_scholarship.html' , form = form)

@admin.route('/delete_scholarship/<int:scholarship_id>' , methods = ['POST' , 'GET'])
def delete_scholarship(scholarship_id):
    scholarship_to_delete = Scholarships.query.get(scholarship_id)
    db.session.delete(scholarship_to_delete)
    db.session.commit()
    flash('scholarship deleted successfully')
    print('scholarship deleted')
    return redirect(url_for('views.home'))


#learning materials
@admin.route('/add_file' , methods = ['POST' , 'GET'])
def add_file():
    form = FilesForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            new_file = Files(title = title, link = link, image = file_path)
            db.session.add(new_file)
            db.session.commit()
            flash('new file added successfully!')
            print('new file added successfully')
            return redirect(url_for('views.home'))
        
        else:
            print('file not added, please try again')
            flash('file not added, please try again')


    
    return render_template('add_file.html' , form = form)


@admin.route('/edit_file/<int:file_id>' , methods = ['POST' , 'GET'])
def edit_file(file_id):
    files = Files.query.get_or_404(file_id)
    form = FilesForm(obj = files)
    if form.validate_on_submit():
        title = request.form.get("title")
        link = request.form.get("link")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)
            Files.query.filter_by(id = file_id).update(dict(title = title, link = link, image = file_path))
            db.session.commit()
            flash('file successfully updated')
            print("successfully updated")
            return redirect(url_for('views.home'))
        

        else:
            flash('file not updated, pleas try again')
            print('file not updated!')

        return render_template('edit_file.html' , form = form)

@admin.route('/delete_file/<int:file_id>' , methods = ['POST' , 'GET'])
def delete_file(file_id):
    file_to_delete = Files.query.get(file_id)
    db.session.delete(file_to_delete)
    db.session.commit()
    flash('file deleted successfully')
    print('file deleted')
    return redirect(url_for('views.home'))
    

#blogs
@admin.route('/add_blog' , methods = ['POST' , 'GET'])
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            new_blog = Blog(title = title, body = body, image = file_path)
            db.session.add(new_blog)
            db.session.commit()
            flash('new blog added successfully!')
            print('new blog added successfully')
            return redirect(url_for('views.home'))
        
        else:
            print('blog not added, please try again')
            flash('blog not added, please try again')


    
    return render_template('add_blog.html' , form = form)

@admin.route('/edit_blog/<int:blog_id>' , methods = ['POST' , 'GET'])
def edit_blog(blog_id):
    blogs = Blog.query.get_or_404(blog_id)
    form = BlogForm(obj = blogs)
    if form.validate_on_submit():
        title = request.form.get("title")
        body = request.form.get("body")
        file = form.image.data
        if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)
            Blog.query.filter_by(id = blog_id).update(dict(title = title, body = body, image = file_path))
            db.session.commit()
            flash('blog successfully updated')
            print("successfully updated")
            return redirect(url_for('views.home'))
        

        else:
            flash('blog not updated, pleas try again')
            print('blog not updated!')

        return render_template('edit_blog.html' , form = form)

@admin.route('/delete_blog/<int:blog_id>' , methods = ['POST' , 'GET'])
def delete_blog(blog_id):
    blog_to_delete = Blog.query.get(blog_id)
    db.session.delete(blog_to_delete)
    db.session.commit()
    flash('blog deleted successfully')
    print('blog deleted')
    return redirect(url_for('views.home'))

@admin.route('/add_gallery')
def add_gallery():
    form = GalleryForm()
    if form.validate_on_submit():
         file = form.image.data
         if file and file.filename:
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)
            new_gallery = Gallery(image = file_path)
            db.session.add(new_gallery)
            db.session.commit()
            flash("New gallery added successfully!")
            print("new gallery added!")

            return redirect(url_for('views.home'))
         
         else:
             flash('gallery not added')
             print('gallery not added')

    
    return render_template('add_gallery.html' , form = form)

@admin.route('delete_gallery/<int:gallery_id>')
def delete_gallery(gallery_id):
    gallery_to_delete = Gallery.query.get(gallery_id)
    db.session.delete(gallery_to_delete)
    db.session.commit()
    flash('gallery deleted successfully!')
    print("gallery deleted!")







