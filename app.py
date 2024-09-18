from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

# Initialize Flask app and load configurations
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy and JWT
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import database models
from models import User

# User registration route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate a JWT token
    access_token = create_access_token(identity={'username': user.username})
    return jsonify(access_token=access_token)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
