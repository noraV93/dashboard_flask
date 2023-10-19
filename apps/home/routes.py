from flask import render_template, session
from ..auth.user import User
from . import home_bp

@home_bp.route('/')
def index():
    # Check if user is logged in
    username = session.get('username')
    is_admin = session.get('is_admin')
    # Fetch all users from database
    users = User.query.all()
    # Render template with data
    if is_admin:
        return render_template('index.html', users=users, username='admin')
    else:
        return render_template('index.html', users=users, username=username)

@home_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@home_bp.route('/maps')
def maps():
    return render_template('maps.html')

@home_bp.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')