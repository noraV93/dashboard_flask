from flask import Blueprint, render_template, session
from ..auth.user import User
from . import home_bp

home_bp = Blueprint('home', __name__, template_folder='templates')

from .dashboard import *
from .maps import *
from .user_profile import *

@home_bp.route('/')
def index():
    # Check if user is logged in
    username = session.get('username')
    is_admin = session.get('is_admin')
    # Render template with data
    if is_admin:
        return render_template('index.html', username='admin')
    else:
        return render_template('index.html', username=username)