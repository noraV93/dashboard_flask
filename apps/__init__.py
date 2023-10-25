import os

from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from apps.config import Config
from apps.auth.user import db, migrate, login_manager, User
from apps.auth.admin_views import UserAdminView
from .auth.routes import auth_bp
from .home.routes import home_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Login_manager
    login_manager.init_app(app)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    # Initialize Flask-Admin
    admin = Admin(app, name='Admin', template_mode='bootstrap4')
    admin.add_view(UserAdminView(User, db.session))

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app
