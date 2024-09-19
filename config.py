import os

class Config:
    # Secret key for signing JWT tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    
    # PostgreSQL database connection
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/sustainability_tracker_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
