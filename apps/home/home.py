from flask import Blueprint, render_template, session
from ..models import User

home_bp = Blueprint('home', __name__)

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