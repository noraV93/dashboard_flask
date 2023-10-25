from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash

from .user import User, db

class UserAdminView(ModelView):
    column_list = ['id', 'username', 'company', 'email']
    form_columns = ['username', 'password', 'company', 'email']
    column_searchable_list = ['username', 'company', 'email']  # Fields that can be searched
    column_sortable_list = ['id', 'username', 'company', 'email']  # Fields that can be sorted

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        flash('You do not have permission to access this page.')
        return redirect(url_for('auth.login'))
