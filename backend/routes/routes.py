from flask import Blueprint
from backend.controller.controller import Controller

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['GET'])(Controller.get_all_users)
user_bp.route('/users/<int:user_id>', methods=['GET'])(Controller.get_user_by_id)
user_bp.route('/users', methods=['POST'])(Controller.create_user)
user_bp.route('/users/<int:user_id>', methods=['PUT'])(Controller.update_user)
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(Controller.delete_user)