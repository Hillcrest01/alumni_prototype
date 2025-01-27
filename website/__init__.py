from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ubblbjbbjkbl'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page'

    from .views import views
    from .auth import auth
    from .admin import admin
    from .alumni import alumni


    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    app.register_blueprint(admin, url_prefix = '/')
    app.register_blueprint(alumni, url_prefix = '/')


    with app.app_context():
        db.create_all()
        print("database created successfully")
    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))