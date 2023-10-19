from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from ..auth.user import User
from . import home_bp
from .. import db

@home_bp.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    if request.method == 'POST':
        # Get form data
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        # Verify old password
        if not current_user.verify_password(old_password):
            flash('Old password is incorrect.', 'error')
            return redirect(url_for('home.user_profile'))
        # Verify new password
        if new_password != confirm_password:
            flash('New password and confirm password do not match.', 'error')
            return redirect(url_for('home.user_profile'))
        # Update user password
        current_user.set_password(new_password)
        db.session.commit()
        flash('Password updated successfully.', 'success')
        return redirect(url_for('home.user_profile'))
    else:
        return render_template('user_profile.html')