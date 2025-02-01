from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileRequired


#forms for authorization for both admin and students login
class SignUpForm(FlaskForm):
    regno = StringField("registration number" , validators=[DataRequired()])
    year_of_study = IntegerField("year of study" , validators=[DataRequired()])
    email_address = EmailField("email address" , validators=[DataRequired()])
    password1 = PasswordField("Password" , validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('confirm password' , validators=[DataRequired()])
    sign_up = SubmitField('sign up' , validators=[DataRequired()])

class LoginForm(FlaskForm):
    regno = StringField("Registration Number" , validators=[DataRequired()])
    password = PasswordField("Password" , validators=[DataRequired()])
    log_in = SubmitField("login" , validators=[DataRequired()])

#forms for adding the mini data on the homepage




#forms for adding data on the pages ...
#the form for admin for adding the jobs
class JobsForm(FlaskForm):
    title = StringField('Job Title' , validators=[DataRequired()] )
    body = StringField('Body' , validators=[DataRequired()])
    location = StringField('Location' , validators=[DataRequired()])
    job_type = SelectField("Which Opportunity" , choices=[('job' , 'job') , ('internship' , 'internship')])
    link = StringField ('Link to this page' , validators=[DataRequired()])
    image = FileField('Add a photo' , validators=[FileRequired()])
    add_job = SubmitField('Add an opportunity')

class EventForm(FlaskForm):
    title = StringField('Event Title' , validators=[DataRequired()] )
    body = StringField('Body' , validators=[DataRequired()])
    location = StringField('Location' , validators=[DataRequired()])
    link = StringField ('Link to this page' , validators=[DataRequired()])
    image = FileField('Add a photo' , validators=[FileRequired()])
    add_event = SubmitField('Add an event')

class ScholarshipForm(FlaskForm):
    title = StringField('Scholarship Title' , validators=[DataRequired()] )
    body = StringField('Body')
    country = StringField('Which Country' , validators=[DataRequired()])
    university = StringField('Which University' , validators=[DataRequired()])
    link = StringField ('Link to this page' , validators=[DataRequired()])
    image = FileField('Add a photo' , validators=[FileRequired()])
    add_scholarship = SubmitField('Add a Scholarship')

class FilesForm(FlaskForm):
    title = StringField('Enter the title of the file' , validators=[DataRequired()])
    link = StringField('Enter the link to the file' , validators=[ DataRequired() ])
    image = FileField('Add a Photo')
    add_files = SubmitField('submit files')

class GalleryForm(FlaskForm):
    image = FileField("Add the images")
    add_image = SubmitField('Add Image')
 

class BlogForm(FlaskForm):
    title = StringField("Enter the blog title" , validators=[DataRequired()])
    body = StringField("Enter your blog content")
    image = FileField("Add an image for the blog" , validators=[FileRequired()])
    add_blog = SubmitField("Add Blog")

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Current Password" , validators= [DataRequired()])
    new_password = PasswordField("New Password" , validators=[DataRequired()])
    confirm_password = PasswordField("Confirm New Password" , validators=[DataRequired(), EqualTo('new_password' , message='passwords do not match!')])
    submit = SubmitField('Change Password')


