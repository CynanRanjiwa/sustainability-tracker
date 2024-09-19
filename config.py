# config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # For JWT secret key
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Database connection
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'anothersecretkey')  # For JWT tokens
