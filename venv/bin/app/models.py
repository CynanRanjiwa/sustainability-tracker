from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Hash the password before saving
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password validity
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Business Model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

# SustainabilityPractice Model
class SustainabilityPractice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Report Model
class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    practice_id = db.Column(db.Integer, db.ForeignKey('sustainability_practice.id'), nullable=False)
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=True)
    
    # Relationships
    business = db.relationship('Business', backref=db.backref('reports', lazy=True))
    practice = db.relationship('SustainabilityPractice', backref=db.backref('reports', lazy=True))
