import os
from flask import Flask, render_template, request, redirect, session
from apps.config import Config
from apps.models import db
from apps.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = 'your-secret-key'

    # Initialize SQLAlchemy
    db.init_app(app)

    # Define login route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['username'] = username
                return redirect('/')
            else:
                return render_template('login.html', error='Invalid username or password')
        else:
            return render_template('login.html')

    # Define routes
    @app.route('/')
    def index():
        # Check if user is logged in
        username = session.get('username')
        # Fetch all users from database
        users = User.query.all()
        # Render template with data
        return render_template('index.html', users=users, username=username)

    return app