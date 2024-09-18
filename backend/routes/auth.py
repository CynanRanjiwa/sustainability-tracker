from flask import Blueprint, request, jsonify
from app import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

# User Registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"})

# User Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT Token
    access_token = create_access_token(identity={'username': user.username})
    return jsonify({"access_token": access_token})


"""

Explanation:

    Register Route: Takes in username, email, and password, hashes the password, and stores it in the database.
    Login Route: Authenticates the user by comparing the hashed password and returns a JWT token if successful
"""