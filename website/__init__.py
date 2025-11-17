from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_limiter import Limiter 
from flask_limiter.util import get_remote_address  

db = SQLAlchemy()
DB_NAME = "database.db"

limiter = Limiter(
    key_func=get_remote_address,  # IP cím alapján
    default_limits=["200 per day", "50 per hour"],  # Alapértelmezett limitek
    storage_uri="memory://"  
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'webfejlesztes'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    limiter.init_app(app)

    from .views import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Book, Reading_List, Review

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')