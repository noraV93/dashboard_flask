from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash

from .user import User, db

class UserAdminView(ModelView):
    column_list = ['id', 'username']  # Columns to display in the list view
    form_columns = ['username', 'password']  # Fields to display in the add/edit forms

    def is_accessible(self):
        # Ensure the user is authenticated and has admin privileges
        return current_user.is_authenticated and current_user.role == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        # Redirect unauthorized users to the login page
        flash('You do not have permission to access this page.')
        return redirect(url_for('auth.login'))
