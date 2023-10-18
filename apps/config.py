import os

class Config:

    SECRET_KEY = 'your-secret-key'

    # MySQL configuration
    SQLALCHEMY_DATABASE_URI = 'mysql://debian-sys-maint:JyzkXoKPeruI9oGe@localhost/mydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENV = 'development'
    DEBUG = True