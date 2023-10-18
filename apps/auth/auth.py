from flask import Blueprint, render_template, request, redirect, session
from ..models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            if user.role == 'admin':
                session['is_admin'] = True
                return redirect('/')
            else:
                session['is_admin'] = False
                return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect('/login')