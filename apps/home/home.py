from flask import Blueprint, render_template, session
from ..models import User

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    # Check if user is logged in
    username = session.get('username')
    # Fetch all users from database
    users = User.query.all()
    # Render template with data
    return render_template('index.html', users=users, username=username)