from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from .forms import SignUpForm, LoginForm, ChangePasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth' , __name__)

@auth.route('/signup' , methods = ['GET' , 'POST'])
def sign_up():

    form = SignUpForm()
    if form.validate_on_submit():
        regno = request.form.get('regno')
        username = request.form.get('username')
        year_of_study = request.form.get('year_of_study')
        email_address = request.form.get('email_address')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        year_of_study = int(year_of_study)

        new_user = User.query.filter_by(regno = regno).first()
        if new_user:
            flash("User already exists! Log in or try a new reg. number" , "error")
            print("Email Already exists")
        
        elif password1 != password2:
            flash("the passwords do not match" , "error")
            print("Wrong Password")


        elif year_of_study < 1:
                flash("Year of study should be at least one" , "error")
                print("invalid year of study")

        elif year_of_study > 4:
                flash("Year of study should not be more than 4" , "error")
                print("Invalid year of study")
        else:
                new_user  = User(regno = regno , username = username, year_of_study = year_of_study, email_address = email_address, password_hash = generate_password_hash(password1) )
                db.session.add(new_user)
                db.session.commit()
                flash("Account created successfully" , "success")
                print("new user added to database")
                return redirect(url_for('auth.login'))



    return render_template('signup.html' , form = form, new_user = current_user)


@auth.route('/login' , methods = ['GET' , 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        regno = request.form.get('regno')
        password = request.form.get('password')

        new_user = User.query.filter_by(regno = regno).first()
        if new_user:
            if check_password_hash(new_user.password_hash, password):
                flash("login successful" , "success")
                print("successful")
                login_user(new_user, remember=True)
                return redirect(url_for('views.profile'))
            
            else:
                flash('incorrect password' , "error")
                print('login failed')
        
        else:
            flash("no account linked with this reg number" , "error")
            print('no reg number linked')

    return render_template('login.html' , form = form , new_user = current_user)


@auth.route('/change_password' , methods = ['POST' , 'GET'])
@login_required

def change_password():
     form = ChangePasswordForm()
     if form.validate_on_submit():
          if not current_user.check_password(form.current_password.data):
               flash("Current password is incorrect" , "error")
          else:
               current_user.set_password(form.new_password.data)
               db.session.commit()
               flash("Your password has been updated" , "success")
               return redirect(url_for('views.profile'))
    

     return render_template("change_password.html" , form = form)

               
        


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you have successfully logged out", "success")
    return redirect(url_for('views.home'))