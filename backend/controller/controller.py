from flask import request, jsonify
from backend.model.user import UserModel
from backend.globals import ROLES

class Controller:
    @staticmethod
    def get_roles():
        return jsonify(ROLES), 200

    @staticmethod
    def get_all_users():
        users = UserModel.get_all_users()
        return jsonify([user.to_dict() for user in users]), 200
    
    @staticmethod
    def get_user_by_id(id):
        user = UserModel.get_user_by_id(id)
        if user:
            return jsonify(user.to_dict()), 200
        return jsonify({"error_message": f"User with id: {id} not found"}), 404
    
    @staticmethod
    def create_user():
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'role' not in data:
            return jsonify({"error_message": "Missing field"}), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        role = data['role'].strip()

        if role not in ROLES:
            return jsonify({"error_message": "Invalid role"}), 400
        
        user = UserModel.create_user(name, email, role)
        return jsonify(user.to_dict()), 201
    
    @staticmethod
    def update_user(id):
        user = UserModel.get_user_by_id(id)
        if not user:
            return jsonify({"error_message": f"User with id: {id} not found"}), 404
        
        data = request.get_json()
        name = data.get('name', user.name).strip()
        email = data.get('email', user.email).strip()
        role = data.get('role', user.role).strip()

        if role not in ROLES:
            return jsonify({"error_message": "Invalid role"}), 400
        
        updated_user = UserModel.update_user(user, name, email, role)
        return jsonify(updated_user.to_dict()), 200
    
    @staticmethod
    def delete_user(id):
        user = UserModel.get_user_by_id(id)
        if not user:
            return jsonify({"error_message": f"User with id: {id} not found"}), 404
        
        UserModel.delete_user(user)
        return jsonify({"message": f"User {id} deleted"}), 200