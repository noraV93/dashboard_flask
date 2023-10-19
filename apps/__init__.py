import os

from flask import Flask, render_template, request, redirect, session
from apps.config import Config
from apps.auth.user import db, migrate

from .auth.routes import auth_bp
from .home.routes import home_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app