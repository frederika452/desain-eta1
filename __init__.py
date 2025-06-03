from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager # type: ignore
from flask_wtf.csrf import CSRFProtect # type: ignore
import os

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rahasia123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    login_manager.login_view = 'main.login'

    return app
