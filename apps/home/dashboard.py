from flask import render_template
from ..auth.user import User
from . import home_bp

@home_bp.route('/dashboard')
def dashboard():
    # Fetch all users from database
    users = User.query.all()
    # Render template with data
    return render_template('dashboard.html', users=users)