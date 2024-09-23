from flask import Blueprint, jsonify, request
from app.models import Business, SustainabilityPractice, Report
from app import db
from flask_jwt_extended import jwt_required

main = Blueprint('main', __name__)

# Get all businesses
@main.route('/businesses', methods=['GET'])
@jwt_required()
def get_businesses():
    businesses = Business.query.all()
    result = [{"id": b.id, "name": b.name, "description": b.description} for b in businesses]
    return jsonify(result), 200

# Add a new business
@main.route('/businesses', methods=['POST'])
@jwt_required()
def add_business():
    data = request.get_json()
    new_business = Business(name=data['name'], description=data.get('description', ''))
    db.session.add(new_business)
    db.session.commit()
    return jsonify({"msg": "Business added"}), 201

# Get all sustainability practices
@main.route('/practices', methods=['GET'])
@jwt_required()
def get_practices():
    practices = SustainabilityPractice.query.all()
    result = [{"id": p.id, "name": p.name, "description": p.description} for p in practices]
    return jsonify(result), 200
