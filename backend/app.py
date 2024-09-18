from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

# Initialize the app and extensions
app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from config.py

# Initialize SQLAlchemy for database and JWT for authentication
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import and register routes
from routes.auth import auth_bp
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
