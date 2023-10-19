from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(64), default='user')
    company = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, role='user', company=None, email=None):
        self.username = username
        self.password = password
        self.role = role
        self.company = company
        self.email = email

    def is_active(self):
        return True
    
    def set_password(self, password):
        self.password = password

    def verify_password(self, password):
        if self.password == password:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % self.username
    
@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None