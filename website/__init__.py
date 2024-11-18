from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ubblbjbbjkbl'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

    db.init_app(app)

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