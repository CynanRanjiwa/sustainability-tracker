from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Relationships
    businesses = db.relationship('Business', backref='owner', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

    # Relationships
    sustainability_practices = db.relationship('SustainabilityPractices', backref='business', lazy=True)

    def __repr__(self):
        return f'<Business {self.name}>'

# Sustainability Practices model
class SustainabilityPractices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    practice = db.Column(db.String(100), nullable=False)
    carbon_footprint = db.Column(db.Float, nullable=False)  # Mock value for now
    business_id = db.Column(db.Integer, ForeignKey('business.id'), nullable=False)

    def __repr__(self):
        return f'<SustainabilityPractices {self.practice}>'

# Reports model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_data = db.Column(db.Text, nullable=False)
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    business_id = db.Column(db.Integer, ForeignKey('business.id'), nullable=False)

    def __repr__(self):
        return f'<Report {self.id}>'


"""
Explanation:

    User table holds user details (username, email, and password).
    Business is linked to a User (a business belongs to a user).
    SustainabilityPractices holds data related to the carbon footprint and other sustainable practices.
    Report stores sustainability reports generated for a business.

"""