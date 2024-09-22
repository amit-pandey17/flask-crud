from flask import Blueprint
from controller.controller import Controller

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    return Controller.get_all_users()

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return Controller.get_user_by_id(user_id)

@user_bp.route('/users', methods=['POST'])
def create_user():
    return Controller.create_user()

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return Controller.update_user(user_id)

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return Controller.delete_user()