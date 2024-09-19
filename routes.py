# files contains user registration login and fetching sustainability data
# routes.py

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import db, User, Business, SustainabilityPractice, Report
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
jwt = JWTManager(app)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], email=data['email'], password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login failed! Check your email and password.'}), 401

    access_token = create_access_token(identity={'username': user.username, 'email': user.email})
    return jsonify({'token': access_token}), 200

@app.route('/carbon-footprint', methods=['GET'])
@jwt_required()
def get_carbon_footprint():
    # Mock data for demonstration purposes
    data = {
        'carbon_footprint': 50.5,  # This could be fetched from a real source
        'unit': 'kg CO2'
    }
    return jsonify(data), 200

# To avoid circular imports, make sure this is the last line
if __name__ == '__main__':
    app.run(debug=True)
