from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from .forms import SignUpForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required, LoginManager

auth = Blueprint('auth' , __name__)

@auth.route('/signup' , methods = ['GET' , 'POST'])
def sign_up():

    form = SignUpForm()
    if form.validate_on_submit():
        regno = request.form.get('regno')
        year_of_study = request.form.get('year_of_study')
        email_address = request.form.get('email_address')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        new_user = User.query.filter_by(regno = regno).first()
        if new_user:
            flash("User already exists! Log in or try a new email address")
            print("Email Already exists")
        
        elif password1 != password2:
            flash("passwords do not match")
            print("Wrong Password")
        
        else:
            new_user  = User(regno = regno , year_of_study = year_of_study, email_address = email_address, password_hash = generate_password_hash(password1) )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully")
            login_user(new_user, remember=True)
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
                flash("login successful")
                print("successful")
                return redirect(url_for('views.home'))
            
            else:
                flash('incorrect password')
                print('login failed')
        
        else:
            flash("no account linked with this reg number")
            print('no reg number linked')

    return render_template('login.html' , form = form , new_user = current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("you have successfully logged out")
    return redirect(url_for('/'))

@auth.route('/profile')
def profile():
    return render_template('profile.html')