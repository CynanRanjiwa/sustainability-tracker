from flask import Flask 
from flask_sqlalchemy import SQLALCHEMY
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv 
import os 

# load environment variables
load_dotenv()

# initialize extensions 
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app= Flask(__name__)

    # configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # register routes 
    from app.routes import main
    app.register_blueprint(main)

    return app

