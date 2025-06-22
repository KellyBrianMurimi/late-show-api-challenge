from flask import request, jsonify
from flask_jwt_extended import create_access_token
from ..models import db, User, jwt
from ..controllers import api

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password required"}), 400
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400
    
    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "User created successfully"}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()
    
    if not user or not user.check_password(data.get('password')):
        return jsonify({"message": "Invalid credentials"}), 401
    
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200