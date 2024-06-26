# app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    #db.create_all()
    from .views import main_bp
    app.register_blueprint(main_bp)

    return app
