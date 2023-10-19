from flask import render_template
from . import home_bp

@home_bp.route('/maps')
def maps():
    return render_template('maps.html')