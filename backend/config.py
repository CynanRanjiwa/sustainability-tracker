# file for database connection and secret keys 
import os

class Config:
    # Secret key for JWT tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'

    # PostgreSQL Database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/sustainability_tracker_db'
    
    # Disable SQLAlchemy track modifications to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False


"""
Explanation:

    SECRET_KEY is used to sign JWT tokens. Replace 'super-secret-key' with something more secure.
    SQLALCHEMY_DATABASE_URI defines the connection string to your PostgreSQL database. Replace username, password, and sustainability_tracker_db with your actual database credentials.

"""