# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes import app as routes_app
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

with app.app_context():
    db.create_all()  # This creates all the tables in the database

app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=True)
